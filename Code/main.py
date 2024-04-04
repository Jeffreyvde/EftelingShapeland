from park_utils import *
from simulation_utils import *

TOTAL_DAILY_AGENTS = 40000
PERFECT_ARRIVALS = True
HOURLY_PERCENT = {
    "10:00 AM": 10,
    "11:00 AM": 20,
    "12:00 AM": 17,
    "3:00 PM": 20,
    "4:00 PM": 15,
    "5:00 PM": 10,
    "6:00 PM": 1,
    "7:00 PM": 5,
    "8:00 PM": 1,
    "9:00 PM": 1,
    "10:00 PM": 0,
    "11:00 PM": 0,
    "12:00 PM": 0
}
EXP_ABILITY_PCT = 1.0
EXP_THRESHOLD = 1
EXP_LIMIT = 3

AGENT_ARCHETYPE_DISTRIBUTION = {
    "ride_enthusiast": 0,
    "ride_favorer": 15,
    "park_tourer": 15,
    "park_visitor": 50,
    "activity_favorer": 10,
    "activity_enthusiast": 10,
}

ATTRACTIONS = [
    {
        "name": "Python",
        "run_time": 2,  # 2.133
        "hourly_throughput": 1440,
        "popularity": 7,  # 6.751
        "expedited_queue": True,  #
        "expedited_queue_ratio": 0.99,
        "child_eligible": True,
        "adult_eligible": True,
        "expected_wait_time": 45,
    },
    {
        "name": "Joris en de Draak",
        "run_time": 2,
        "hourly_throughput": 1700,
        "popularity": 9,  # 9.163
        "expedited_queue": True,  #
        "expedited_queue_ratio": 0.99,
        "child_eligible": True,
        "adult_eligible": True,
        "expected_wait_time": 56,
    },
    {
        "name": "Vliegende Hollander",
        "run_time": 4,  # 3.7167
        "hourly_throughput": 1900,
        "popularity": 10,
        "expedited_queue": True,  #
        "expedited_queue_ratio": 0.99,
        "child_eligible": True,
        "adult_eligible": True,
        "expected_wait_time": 53.4,
    },
    {
        "name": "Baron 1898",
        "run_time": 2,  # 2.16666666666
        "hourly_throughput": 900,
        "popularity": 4,  # 4.490
        "expedited_queue": False,
        "expedited_queue_ratio": 0.8,
        "child_eligible": True,
        "adult_eligible": True,
        "expected_wait_time": 59.5,
    },
    {
        "name": "Kinderspoor",
        "run_time": 2,
        "hourly_throughput": 420,
        "popularity": 1,  # 1.096
        "expedited_queue": False,
        "expedited_queue_ratio": 0.8,
        "child_eligible": True,
        "adult_eligible": False,
        "expected_wait_time": 21,
    },
    {
        "name": "De oude tufferbaan",
        "run_time": 4,
        "hourly_throughput": 1200,
        "popularity": 5,  # 5.083
        "expedited_queue": False,
        "expedited_queue_ratio": 0.8,
        "child_eligible": True,
        "adult_eligible": True,
        "expected_wait_time": 30,
    },
    {
        "name": "Halve maan",
        "run_time": 3,
        "hourly_throughput": 1200,
        "popularity": 5,  # 4.698
        "expedited_queue": False,
        "expedited_queue_ratio": 0.8,
        "child_eligible": True,
        "adult_eligible": True,
        "expected_wait_time": 31.4,
    },
    {
        "name": "Pirana",
        "run_time": 7,  # 6.5
        "hourly_throughput": 2000,
        "popularity": 9,  # 8.954
        "expedited_queue": True,  #
        "expedited_queue_ratio": 0.99,
        "child_eligible": True,
        "adult_eligible": True,
        "expected_wait_time": 36.4,
    },
    {
        "name": "Max & Moritz",
        "run_time": 2,  # 1.5
        "hourly_throughput": 1800,
        "popularity": 8,  # 8.194
        "expedited_queue": False,
        "expedited_queue_ratio": 0.8,
        "child_eligible": True,
        "adult_eligible": True,
        "expected_wait_time": 41.4,
    },
    {
        "name": "Fata Morgana",
        "run_time": 8,
        "hourly_throughput": 1600,
        "popularity": 7,  # 7.306
        "expedited_queue": False,
        "expedited_queue_ratio": 0.8,
        "child_eligible": True,
        "adult_eligible": True,
        "expected_wait_time": 29.3,
    },
    {
        "name": "Fabula",
        "run_time": 17,
        "hourly_throughput": 1760,
        "popularity": 7,  # 6.587
        "expedited_queue": False,
        "expedited_queue_ratio": 0.8,
        "child_eligible": True,
        "adult_eligible": True,
        "expected_wait_time": 16.7,
    },
    {
        "name": "Volk_van_Laaf_(Monorail)",
        "run_time": 7,
        "hourly_throughput": 425,
        "popularity": 1,  # 1.391
        "expedited_queue": False,
        "expedited_queue_ratio": 0.8,
        "child_eligible": True,
        "adult_eligible": True,
        "expected_wait_time": 30.4,
    },
    {
        "name": "Stoomcarrousel",
        "run_time": 2,
        "hourly_throughput": 400,
        "popularity": 1,
        "expedited_queue": False,
        "expedited_queue_ratio": 0.8,
        "child_eligible": True,
        "adult_eligible": True,
        "expected_wait_time": 16,
    },
    {
        "name": "Droomvlucht",
        "run_time": 6,
        "hourly_throughput": 1775,
        "popularity": 8,  # 8.233
        "expedited_queue": False,
        "expedited_queue_ratio": 0.8,
        "child_eligible": True,
        "adult_eligible": True,
        "expected_wait_time": 44.4,
    },
    {
        "name": "Villa_Volta",
        "run_time": 10,
        "hourly_throughput": 1200,
        "popularity": 5,  # 4.698
        "expedited_queue": False,
        "expedited_queue_ratio": 0.8,
        "child_eligible": True,
        "adult_eligible": True,
        "expected_wait_time": 26,
    },
    {
        "name": "Sirocco",
        "run_time": 8,
        "hourly_throughput": 1000,
        "popularity": 4,  # 3.502
        "expedited_queue": False,
        "expedited_queue_ratio": 0.8,
        "child_eligible": True,
        "adult_eligible": True,
        "expected_wait_time": 20.3,
    },
    {
        "name": "Vogel_Rok",
        "run_time": 2,  # 1.520
        "hourly_throughput": 1600,
        "popularity": 7,  # 6.709
        "expedited_queue": False,
        "expedited_queue_ratio": 0.8,
        "child_eligible": True,
        "adult_eligible": True,
        "expected_wait_time": 32,
    },
    {
        "name": "Carnaval_Festival",
        "run_time": 8,
        "hourly_throughput": 1750,
        "popularity": 7,  # 7.482
        "expedited_queue": False,
        "expedited_queue_ratio": 0.8,
        "child_eligible": True,
        "adult_eligible": True,
        "expected_wait_time": 28.6,
    },
    {
        "name": "Symbolica",
        "run_time": 10,
        "hourly_throughput": 1400,
        "popularity": 7,  # 6.773
        "expedited_queue": True,  #
        "expedited_queue_ratio": 0.99,
        "child_eligible": True,
        "adult_eligible": True,
        "expected_wait_time": 46.6,
    }
]

ACTIVITIES = [
  {
    "name": "sightseeing",
    "popularity": 5,
    "mean_time": 5
  },
  {
    "name": "show",
    "popularity": 5,
    "mean_time": 30
  },
  {
    "name": "merchandise",
    "popularity": 5,
    "mean_time": 30
  },
  {
    "name": "food",
    "popularity": 5,
    "mean_time": 45
  }
]

PLOT_RANGE = {
    "Attraction Queue Length": 40000,
    "Attraction Wait Time": 100,
    "Attraction Expedited Queue Length": 6000,
    "Attraction Expedited Wait Time": 500,
    "Activity Vistors": 20000,
    "Approximate Agent Distribution (General)": 1.0,
    "Approximate Agent Distribution (Specific)": 1.0,
    "Attraction Average Wait Times": 120,
    "Agent Attractions Histogram": 1.0,
    "Attraction Total Visits": 46000,
    "Expedited Pass Distribution": 150000,
    "Age Class Distribution": 20000,
}

if __name__ == '__main__':
    runs = 32
    print(f"Running the simulation {runs} times")
    results = run_multiple_simulations(runs, HOURLY_PERCENT, ATTRACTIONS, ACTIVITIES, PLOT_RANGE, TOTAL_DAILY_AGENTS, PERFECT_ARRIVALS, AGENT_ARCHETYPE_DISTRIBUTION, EXP_ABILITY_PCT, EXP_THRESHOLD, EXP_LIMIT)
    # Run simulations without

