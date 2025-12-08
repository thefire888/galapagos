use pyo3::prelude::*;
use pyo3::types::PyList;
use std::collections::HashMap;

use crate::individual::Individual;
use crate::utils;

type PopulationEntry = (Individual, u32);

#[pyclass(subclass, module = "galapagos_evo")]
pub struct Generation {
    #[pyo3(get, set)]
    pub population: Vec<PopulationEntry>, 
    
    __genepool: Py<PyList>, 

    #[pyo3(get, set)]
    pub duplication_chance: f64,
    
    #[pyo3(get, set)]
    pub mutation_chance: f64,
    
    #[pyo3(get, set)]
    pub equal_mutation_odds: bool,
}

#[pymethods]
impl Generation {
    #[new]
    #[pyo3(signature = (population, genepool, duplication_chance=0.0, mutation_chance=0.0, equal_mutation_odds=false))]
    fn new(population: Option<Vec<PopulationEntry>>,
           genepool: Py<PyList>,
           duplication_chance: Option<f64>,
           mutation_chance: Option<f64>,
           equal_mutation_odds: Option<bool>) -> Self {
        
        Generation {
            population: population.unwrap_or_default(),
            __genepool: genepool,
            duplication_chance: duplication_chance.unwrap_or(0.0),
            mutation_chance: mutation_chance.unwrap_or(0.0),
            equal_mutation_odds: equal_mutation_odds.unwrap_or(false),
        }
    }

    fn __len__(&self) -> usize {
        self.population.iter()
            .map(|(_, count)| *count as usize)
            .sum()
    }

    fn __getitem__(&self, key: usize) -> PyResult<PopulationEntry> {
        self.population.get(key)
            .cloned()
            .ok_or_else(|| pyo3::exceptions::PyIndexError::new_err("Index out of bounds"))
    }

    fn __setitem__(&mut self, key: usize, value: PopulationEntry) -> PyResult<()> {
        if key < self.population.len() {
            self.population[key] = value;
            Ok(())
        } else {
            Err(pyo3::exceptions::PyIndexError::new_err("Index out of bounds"))
        }
    }

    pub fn __str__(&self) -> String {
        self.population.iter()
            .map(|(individual, count)| {
                format!("Indivíduo: {} Quantidade: {}", individual.__str__(), count)
            })
            .collect::<Vec<String>>()
            .join("\n")
    }

    #[getter]
    fn genepool(&self, py: Python<'_>) -> Py<PyList> {
        self.__genepool.clone_ref(py)
    }
    
    fn next(&self, py: Python<'_>) -> PyResult<Self> {
        let mut next_gen = Generation::new(
            None, // population vazia
            self.__genepool.clone_ref(py),
            Some(self.duplication_chance),
            Some(self.mutation_chance),
            Some(self.equal_mutation_odds)
        );

        let mut next_gen_individual_counts: HashMap<Individual, u32> = HashMap::new();
        
        let total_size = self.__len__();
        
        for _ in 0..total_size {
            let available_individuals: Vec<(Individual, f64)> = self.population.iter()
            .map(|(ind, count)| (ind.clone(), *count as f64))
            .collect();

            let some_individual = utils::select_individual(&available_individuals)?;
            
            let mut newborn = some_individual.duplicate(
                py,
                next_gen.duplication_chance,
                next_gen.mutation_chance,
                self.__genepool.bind(py),
                next_gen.equal_mutation_odds
            )?;
            
            newborn.update_fitness(self.__genepool.bind(py))?;
            
            *next_gen_individual_counts.entry(newborn).or_insert(0) += 1;
        }

        next_gen.population = next_gen_individual_counts.into_iter()
            .map(|(individual, count)| (individual, count))
            .collect();

        Ok(next_gen)
    }
}
