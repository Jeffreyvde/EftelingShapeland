from park import *
from typing import Tuple
import statistics


def create_park(seed: int, hourly_percent, attractions, activities, plot_range, total_daily_agents, perfect_arrivals,
                agent_archetype_distribution, exp_ability_pct, exp_threshold, exp_limit):
    """
    Create a park with the following settings.
    """
    under_construction_park = Park(
        attraction_list=attractions,
        activity_list=activities,
        plot_range=plot_range,
        random_seed=seed,
        version=None,
        verbosity=False
    )

    # Build Arrivals
    under_construction_park.generate_arrival_schedule(
        arrival_seed=hourly_percent,
        total_daily_agents=total_daily_agents,
        perfect_arrivals=perfect_arrivals,
    )

    # Build Agents
    under_construction_park.generate_agents(
        behavior_archetype_distribution=agent_archetype_distribution,
        exp_ability_pct=exp_ability_pct,
        exp_wait_threshold=exp_threshold,
        exp_limit=exp_limit
    )

    # Build Attractions + Activities
    under_construction_park.generate_attractions()
    under_construction_park.generate_activities()

    return under_construction_park


def reduce_park(park: Park, remove_agents: bool, remove_attractions: bool) -> Park:
    """
    Reduce the parks to only hold the queue data.
    Should only be used after running the simulation.
    """

    # Simplify park
    park.attraction_list = None
    park.activity_list = None
    park.plot_range = None
    park.version = None
    park.schedule = None
    park.activities = None
    park.history = None

    if remove_agents:
        park.agents = None

    if remove_attractions:
        park.attractions = None

    return park


def get_average_wait_times(parks: list[Park]) -> dict[str, float]:
    """
    Get the average wait times from a set of parks
    """
    average_wait_times = {}

    for park in parks:
        park_wait_time = get_park_average_wait_times(park)
        for attraction_name, average_wait_time in park_wait_time.items():
            average_wait_times[attraction_name] = average_wait_times.get(attraction_name, 0) + average_wait_time

    for attraction_name in average_wait_times.keys():
        average_wait_times[attraction_name] = average_wait_times[attraction_name] / len(parks)

    return average_wait_times


def get_park_average_wait_times(park: Park) -> dict[str, float]:
    """
    Get average wait times for rides in park
    """
    average_wait_times = {}
    for attraction_name, attraction in park.attractions.items():
        # Get wait times for attractions before the park closes
        queue_wait_list = [
            val for time, val in attraction.history["queue_wait_time"].items()
            if time <= park.park_close
        ]

        average_wait_times[attraction_name] = sum(queue_wait_list) / len(queue_wait_list)
    return average_wait_times

def get_park_mean_and_std_attraction_visits(park: Park) -> Tuple[float, float]:
    """
    Get the mean and standard deviation attraction visits in a park.
    """
    total_attractions_visited = [
        sum(attraction['times_completed'] for attraction in agent.state["attractions"].values())
        for agent_id, agent in park.agents.items()
    ]
    
    mean_value = statistics.mean(total_attractions_visited)
    std_value = statistics.stdev(total_attractions_visited)

    return mean_value, std_value

def get_mean_and_std_attraction_visits(parks: list[Park]) -> Tuple[float, float]:
    """
    Get the mean and standard deviation of attraction visits for multiple parks.
    """
    means_list = []
    stds_list = []
    for park in parks:
        mean, std = get_park_mean_and_std_attraction_visits(park)
        means_list.append(mean)
        stds_list.append(std)
    
    mean_all_parks = np.mean(means_list)
    std_all_parks = np.mean(stds_list)

    return mean_all_parks, std_all_parks