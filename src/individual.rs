use pyo3::prelude::*;
use pyo3::types::PyList;
use std::hash::{Hash, Hasher};
use std::collections::hash_map::DefaultHasher;
use std::collections::HashMap;

use rand::prelude::*;

use crate::genotype::Genotype;
use crate::locus::Locus; 
use crate::utils; 


#[pyclass(subclass, module = "galapagos_evo")]
#[derive(Clone, PartialEq)] 
pub struct Individual {
    #[pyo3(get)] 
    pub fitness: f64, 
    
    #[pyo3(get)]
    sex: String, 
    
    #[pyo3(get, set)] 
    pub genotype: Genotype,
}

impl std::hash::Hash for Individual {
    fn hash<H: std::hash::Hasher>(&self, state: &mut H) {
        self.fitness.to_bits().hash(state);
        self.sex.hash(state);
        self.genotype.hash(state);
    }
}

impl std::cmp::Eq for Individual {}

#[pymethods]
impl Individual {
    #[new]
    #[pyo3(signature = (sex, genotype, fitness=1.0))]
    pub fn new(sex: String, genotype: Genotype, fitness: Option<f64>) -> Self {
        Individual {
            fitness: fitness.unwrap_or(1.0),
            sex,
            genotype,
        }
    }

    pub fn __str__(&self) -> String {
        format!("Sexo: {} Genótipo: {} Fitness: {}", 
                self.sex, 
                self.genotype.__str__(), 
                self.fitness)
    }

    pub fn __eq__(&self, other: &Self) -> bool {
        (self.fitness == other.fitness) && (self.sex == other.sex) && (self.genotype == other.genotype)
    }

    pub fn __hash__(&self) -> u64 {
        let mut hasher = DefaultHasher::new();
        self.fitness.to_bits().hash(&mut hasher); 
        self.sex.hash(&mut hasher);
        self.genotype.hash(&mut hasher);
        hasher.finish()
    }

    pub fn duplicate(&self, 
             py: Python<'_>,
             duplication_chance: f64,
             mutation_chance: f64,
             genepool: &Bound<'_, PyList>, 
             equal_mutation_odds: bool) -> PyResult<Self> {

        let mut rng = thread_rng();
        let current_genotype = &self.genotype;
        
        let mut new_genotype = current_genotype.clone();
        
        let len = new_genotype.loci.len(); 
        for i in 0..len {
            // Duplicação
            if rng.r#gen::<f64>() < duplication_chance {
                let locus_to_append = new_genotype.loci[i].clone();
                new_genotype.append(locus_to_append);
            }

            // Mutação
            if rng.r#gen::<f64>() < mutation_chance {
                let genepool_rust: Vec<(Locus, f64, f64)> = genepool.extract()?;
                let new_locus_str: String;
                
                if equal_mutation_odds {
                    let gene_to_mutate_tuple = genepool_rust.choose(&mut rng).unwrap();
                    new_locus_str = gene_to_mutate_tuple.0.__str__();
                } else {
                    let options_with_odds: Vec<(String, f64)> = genepool_rust
                        .into_iter()
                        .map(|(l, _, o)| (l.__str__(), o))
                        .collect();
                    
                    new_locus_str = utils::sample_from_distribution(&options_with_odds)?;
                }
                
                let alleles_list: Bound<'_, PyList> = PyList::new(py, [&new_locus_str])?; 
                let new_locus = Locus::new(alleles_list)?;
                
                new_genotype.loci[i] = new_locus;
            }
        }

        let new_sex = utils::random_sex();
        
        Ok(Individual::new(new_sex, new_genotype, Some(1.0)))
    }
    
    pub fn update_fitness(&mut self, genepool: &Bound<'_, PyList>) -> PyResult<()> {
        let genepool_rust: Vec<(Locus, f64, f64)> = genepool.extract()?;

        if genepool_rust.is_empty() {
            return Ok(());
        }

        let fitness_map: HashMap<Locus, f64> = genepool_rust
            .into_iter()
            .map(|(locus, fitness, _odd)| (locus, fitness))
            .collect();

        self.fitness = 1.0;
        let gene_cost = 0.0005;

        for locus in self.genotype.loci.iter() {

            let locus_fitness = fitness_map.get(locus)
                .ok_or_else(|| pyo3::exceptions::PyValueError::new_err(
                    format!("Locus '{}' not found in fitness map", locus.__str__())
                ))?;

            self.fitness *= locus_fitness;
        }

        self.fitness *= 1.0 - gene_cost * self.genotype.loci.len() as f64;

        Ok(())
    }
}
