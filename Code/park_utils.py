from park import Park


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


def reduce_parks(parks):
    """
    Reduce the parks to only hold the queue data.
    """
    return parks
