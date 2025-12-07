use pyo3::prelude::*;
mod locus;

#[pymodule]
fn galapagos_evo(_py: Python, m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<locus::Locus>()?;
    Ok(())
}
