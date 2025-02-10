
import random
import simpy

from Helper import constants as c


class MiningTruck:

    # use class constants considering that all trucks have identical capabilities
    __MIN_MINING_DURATION = 1 * 60
    __MAX_MINING_DURATION = 5 * 60
    __TRAVEL_DURATION = 30
    __UNLOADING_DURATION = 5

    def __init__(self,
                 env: simpy.Environment,
                 unload_station: simpy.Resource,
                 truck_id: int,
                 work_log: dict,
                 verbose: bool):
        self.env = env
        self.unload_station = unload_station
        self.truck_id = truck_id
        self.work_log = work_log
        self.verbose = verbose
        # Start the run process everytime an instance is created
        self.action = env.process(self.run())

    def mine(self):
        # random mining duration
        mining_duration  = random.randint(self.__MIN_MINING_DURATION, self.__MAX_MINING_DURATION + 1)

        if self.verbose:
            print(f'[{self.env.now}] Truck #{self.truck_id} mining for {mining_duration} min')

        # log work: count mining iteration and mining time
        self.work_log[c.MINING_TRUCK][c.PERFORMANCE][self.truck_id] += 1
        self.work_log[c.MINING_TRUCK][c.EFFICIENCY][self.truck_id] += mining_duration

        yield self.env.timeout(mining_duration)

    def travel(self):
        if self.verbose:
            print(f'[{self.env.now}] Truck #{self.truck_id} travel for {self.__TRAVEL_DURATION} min')

        yield self.env.timeout(self.__TRAVEL_DURATION)

    def unload(self):
        if self.verbose:
            print(f'[{self.env.now}] Truck #{self.truck_id} unloading for {self.__UNLOADING_DURATION} min')

        # log work - mining time
        self.work_log[c.UNLOAD_STATION][c.EFFICIENCY] += self.__UNLOADING_DURATION

        yield self.env.timeout(self.__UNLOADING_DURATION)

    def run(self):
        while True:
            yield self.env.process(self.travel())
            yield self.env.process(self.mine())
            yield self.env.process(self.travel())

            # wait for available unload station
            with self.unload_station.request() as resource_request:
                yield resource_request

                # log work - count unloading time
                self.work_log[c.UNLOAD_STATION][c.PERFORMANCE] += 1

                yield self.env.process(self.unload())
