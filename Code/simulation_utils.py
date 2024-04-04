from multiprocessing import cpu_count, Pool

from park import Park


def simulate(park_simulation, hours: int):
    # Pass Time
    minutes_per_hour = 60
    for _ in range(hours * minutes_per_hour):
        park_simulation.step()

    return park_simulation




def run_multiple_simulations(simulation_parks, opening_hours: int, run_count: int):
    print(f"Running simulation on {cpu_count()} cores")

    # Run simulations
    with Pool() as pool:
        sim_results = pool.starmap(simulate, simulation_parks)
    return sim_results
