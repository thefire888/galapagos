use pyo3::prelude::*;
use rand::prelude::*;

use crate::individual::Individual; 

pub fn random_sex() -> String {
    let mut rng = thread_rng();
    if rng.gen_bool(0.5) { 
        "M".to_string()
    } else {
        "F".to_string()
    }
}

pub fn get_total_cumulative_fit(available_individuals: &[(Individual, f64)]) -> f64 {
    available_individuals.iter()
        .map(|(individual, weight)| individual.fitness * weight)
        .sum()
}

pub fn select_individual(available_individuals: &[(Individual, f64)]) -> PyResult<Individual> {
    let total_cumulative_fit = get_total_cumulative_fit(available_individuals);
    
    if total_cumulative_fit <= 0.0 {
        return Err(pyo3::exceptions::PyValueError::new_err(
            "Total cumulative fitness is zero or negative, cannot sample."
        ));
    }
    
    let mut rng = thread_rng();
    let rand = rng.gen_range(0.0..total_cumulative_fit);
    
    let mut cumulative_fit = 0.0;
    for (individual, weight) in available_individuals.iter() {
        cumulative_fit += individual.fitness * weight;
        if cumulative_fit > rand {
            return Ok(individual.clone());
        }
    }
    
    Err(pyo3::exceptions::PyException::new_err(
        "Valor aleatório não mapeia para nenhum indivíduo (Sampling Error)"
    ))
}

pub fn get_max_sample(options_with_odds: &[(String, f64)]) -> f64 {
    options_with_odds.iter()
        .map(|(_, odd)| odd)
        .sum()
}

pub fn sample_from_distribution(options_with_odds: &[(String, f64)]) -> PyResult<String> {
    let max_sample = get_max_sample(options_with_odds);

    if max_sample <= 0.0 {
         return Err(pyo3::exceptions::PyValueError::new_err(
            "Total sampling chance is zero or negative, cannot sample."
        ));
    }

    let mut rng = thread_rng();
    let rand = rng.gen_range(0.0..max_sample);

    let mut sample = 0.0;
    for (option, odd) in options_with_odds.iter() {
        sample += odd;
        if sample > rand {
            return Ok(option.clone());
        }
    }
    
    Err(pyo3::exceptions::PyException::new_err(
        "Valor aleatório não mapeia para nenhuma opção (Sampling Error)"
    ))
}
