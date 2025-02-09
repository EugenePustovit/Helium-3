import simpy
from Components.mining_truck import MiningTruck

mining_trucks_count = 13
mining_unload_stations_count = 7
simulation_time = 72 * 60
# simulation_time = 10 * 60

env = simpy.Environment()
unload_station = simpy.Resource(env, capacity=mining_unload_stations_count)
for i in range(mining_trucks_count):
    MiningTruck(env, unload_station, i)
env.run(until=simulation_time)
