use pyo3::prelude::*;
use std::collections::hash_map::DefaultHasher;
use std::hash::{Hash, Hasher};

use crate::locus::Locus;

#[pyclass(subclass, module = "galapagos_evo")]
#[derive(Clone, Hash, PartialEq, Eq)]
pub struct Genotype {
    #[pyo3(get)] 
    size: usize,
    pub loci: Vec<Locus>, 
}

#[pymethods]
impl Genotype {
    #[new]
    pub fn new(size: usize) -> Self {
        Genotype {
            size,
            loci: Vec::with_capacity(size),
        }
    }

    pub fn __str__(&self) -> String {
        self.loci
            .iter()
            .map(|locus| locus.__str__()) 
            .collect::<Vec<String>>()
            .join(" ") 
    }

    pub fn __len__(&self) -> usize {
        self.size 
    }

    pub fn __getitem__(&self, py: Python<'_>, key: usize) -> PyResult<Py<Locus>> {
        let locus = self.loci
            .get(key)
            .ok_or_else(|| pyo3::exceptions::PyIndexError::new_err("Index out of bounds"))?;

        Ok(Py::new(py, locus.clone())?)
    }

    fn __setitem__(&mut self, key: usize, value: Locus) -> PyResult<()> {
        if key < self.loci.len() {
            self.loci[key] = value;
            Ok(())
        } else if key == self.loci.len() && key < self.size {
            // Permite 'append' se o array ainda não atingiu o 'size'
            self.loci.push(value);
            Ok(())
        } else {
            Err(pyo3::exceptions::PyIndexError::new_err("Index out of bounds or exceeding initial size"))
        }
    }
    
    pub fn append(&mut self, new_value: Locus) {
        self.loci.push(new_value);
        self.size = self.loci.len();
    }

    fn __contains__(&self, locus: &Locus) -> bool {
        self.loci.contains(locus)
    }

    fn __eq__(&self, other: &Self) -> bool {
        self.loci == other.loci
    }

    fn __hash__(&self) -> u64 {
        let mut hasher = DefaultHasher::new();
        self.loci.hash(&mut hasher);
        hasher.finish()
    }
}
