use pyo3::prelude::*;
pub mod locus;
pub mod genotype; 
pub mod individual; 
pub mod utils; 
mod generation; 

#[pymodule]
fn galapagos_evo(_py: Python, m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<locus::Locus>()?;
    m.add_class::<genotype::Genotype>()?;
    m.add_class::<individual::Individual>()?;
    m.add_class::<generation::Generation>()?;

    Ok(())
}
