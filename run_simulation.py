
import simpy

from Components.mining_truck import MiningTruck
from Helper import data_analysis as da
from Helper import cmd

# parse simulation parameters input from command line
args = cmd.parse_cmd_options()

# create work log
work_log = da.report_template(args.truck)

# run simulation
env = simpy.Environment()
unload_station = simpy.Resource(env, capacity=args.station)

for truck_id in range(args.truck):
    MiningTruck(env, unload_station, truck_id, work_log, args.verbose)

env.run(until=args.time * 60)

# generate and print reports
da.calculate_and_report_statistics(work_log, args.verbose)
