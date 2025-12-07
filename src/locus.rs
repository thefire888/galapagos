use pyo3::prelude::*;
use pyo3::types::PyList; 
use std::collections::hash_map::DefaultHasher;
use std::hash::{Hash, Hasher};
use rand::seq::SliceRandom;
use rand::thread_rng;

#[pyclass(subclass, module = "galapagos_evo")]
#[derive(Clone)]
pub struct Locus {
    alleles: Vec<String>,
}

#[pymethods]
impl Locus {
    #[new]
    fn new(alleles: Bound<'_, PyList>) -> PyResult<Self> {
        let alleles_vec: Vec<String> = alleles
            .iter() 
            .map(|item| item.to_string())
            .collect();
            
        Ok(Locus { alleles: alleles_vec })
    }

    fn __str__(&self) -> String {
        let mut canon_alleles = self.alleles.clone();
        canon_alleles.sort();

        canon_alleles.join("")
    }

    fn __eq__(&self, other: &Self) -> bool {
        let set_self: std::collections::HashSet<&String> = self.alleles.iter().collect();
        let set_other: std::collections::HashSet<&String> = other.alleles.iter().collect();

        set_self == set_other
    }

    fn __hash__(&self) -> u64 {
        let mut hasher = DefaultHasher::new();
        let mut sorted_alleles = self.alleles.clone();
        sorted_alleles.sort();
        
        sorted_alleles.hash(&mut hasher);

        hasher.finish()
    }

    fn __getitem__(&self, key: usize) -> PyResult<String> {
        let mut sorted_alleles = self.alleles.clone();
        sorted_alleles.sort();
        
        sorted_alleles
            .get(key) 
            .cloned()
            .ok_or_else(|| pyo3::exceptions::PyIndexError::new_err(format!("Index {} out of bounds", key)))
    }

    fn __len__(&self) -> usize {
        self.alleles.len()
    }

    fn pass_allele(&self) -> PyResult<String> {
        let mut rng = thread_rng();
        let allele = self.alleles.choose(&mut rng).ok_or_else(|| {
            pyo3::exceptions::PyValueError::new_err("Locus must contain at least one allele.")
        })?;

        Ok(allele.clone())
    }
}
