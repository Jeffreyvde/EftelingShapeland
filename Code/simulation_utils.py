from multiprocessing import Pool
from park_utils import *


def simulate(seed: int, hourly_percent, attractions, activities, plot_range, total_daily_agents, perfect_arrivals,
             agent_archetype_distribution, exp_ability_pct, exp_threshold, exp_limit):
    """
    Simulate a set of parks with a given number of hours
    """
    park = create_park(seed, hourly_percent, attractions, activities, plot_range, total_daily_agents, perfect_arrivals,
                       agent_archetype_distribution, exp_ability_pct, exp_threshold, exp_limit)
    print(f"Created Park with {seed}")
    # Pass Time
    minutes_per_hour = 60
    for _ in range(len(hourly_percent) * minutes_per_hour):
        park.step()

    print(f"Simulated park with {seed}")
    return park


def run_multiple_simulations(runs: int, hourly_percent, attractions, activities, plot_range, total_daily_agents,
                             perfect_arrivals,
                             agent_archetype_distribution, exp_ability_pct, exp_threshold, exp_limit):
    """
    Run multiple park simulation with given number of hours on multiple threads
    """

    # Initialize simulator parameters
    simulation_data = []
    run_info = (0, hourly_percent, attractions, activities, plot_range, total_daily_agents, perfect_arrivals,
                agent_archetype_distribution, exp_ability_pct, exp_threshold, exp_limit)
    seed_multiplier = 1000
    for i in range(runs):
        run_information = (i * seed_multiplier,) + run_info[1:]
        simulation_data.append(run_information)

    # Run simulations
    with Pool() as pool:
        return pool.starmap(simulate, simulation_data)
