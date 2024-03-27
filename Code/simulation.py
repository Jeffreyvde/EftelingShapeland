def simulate(park_simulation, hours: int):
    # Pass Time
    minutes_per_hour = 60
    for _ in range(hours * minutes_per_hour):
        park_simulation.step()

    return park_simulation
