import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from typing import Dict, Any
import time

# Simulation parameters
NUM_SIMULATIONS: int = 1_000_000  # Number of Monte Carlo runs
BUDGET: int = 8_500_000_000  # Total budget available
ANNUAL_COST_PER_PERSON: int = 6_000  # Cost per person per year
MAX_COVERAGE: int = BUDGET // ANNUAL_COST_PER_PERSON  # Maximum number of people that can be covered

# Enrollment data with leakage and undercoverage rates
options: Dict[str, Dict[str, Any]] = {
    "Option 1": {"Poor": 637_897, "Not Poor": 221_402, "Leakage": 25.76, "Undercoverage": 65.93},
    "Option 2": {"Poor": 801_537, "Not Poor": 611_645,  "Leakage": 43.28, "Undercoverage": 57.19},
    "Option 3": {"Poor": 1_047_934, "Not Poor": 1_992_910, "Leakage": 65.54, "Undercoverage": 44.03},
}

def monte_carlo_simulation(option_data: Dict[str, Any], num_simulations: int = NUM_SIMULATIONS) -> pd.DataFrame:
    """
    Runs a Monte Carlo simulation to estimate the expected number of poor and not-poor individuals covered
    under budget constraints for a given policy option.
    
    Parameters:
    option_data (Dict[str, Any]): Contains the number of poor and not-poor eligible individuals, leakage, and undercoverage rates.
    num_simulations (int): Number of Monte Carlo simulations to run.
    
    Returns:
    pd.DataFrame: DataFrame containing the simulated coverage results.
    """
    results = []
    
    for _ in range(num_simulations):
        total_enrolled: int = option_data["Poor"] + option_data["Not Poor"]
        
        # Simulate leakage: proportion of not-poor individuals wrongly covered first
        not_poor_covered: int = np.random.binomial(option_data["Not Poor"], option_data["Leakage"] / 100)
        
        # Compute remaining budget after covering wrongly enrolled individuals
        remaining_budget: int = MAX_COVERAGE - not_poor_covered
        
        # Cover as many poor individuals as the remaining budget allows
        poor_covered: int = min(option_data["Poor"], remaining_budget)
        
        # Total individuals covered in this simulation run
        total_covered: int = poor_covered + not_poor_covered
        
        results.append({
            "Poor Covered": poor_covered,
            "Not Poor Covered": not_poor_covered,
            "Total Covered": total_covered,
        })
    
    return pd.DataFrame(results)

def main() -> None:
    """
    Main function to execute Monte Carlo simulations for all policy options and display summary statistics.
    """
    t1 = time.time()
    # Run simulations for all policy options
    simulation_results: Dict[str, pd.DataFrame] = {option: monte_carlo_simulation(data) for option, data in options.items()}
    
    # Compute summary statistics for each option
    summary_stats: Dict[str, pd.DataFrame] = {}
    for option, df in simulation_results.items():
        formatted_stats = df.describe().applymap(lambda x: f"{x:,.2f}")
        summary_stats[option] = formatted_stats
    
    # Display summary statistics for each option
    for option, stats in summary_stats.items():
        print(f"\n{option} Summary Statistics:\n", stats)

    # Display time taken
    print(f"Time taken: {time.time()-t1:.4f} seconds")

if __name__ == "__main__":
    main()