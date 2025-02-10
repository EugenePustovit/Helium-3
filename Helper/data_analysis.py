import pandas as pd

from Helper import constants as c


def report_template(mining_trucks_count: int) -> dict:

    return {
        c.MINING_TRUCK: {
            c.PERFORMANCE: [0] * mining_trucks_count,
            c.EFFICIENCY: [0] * mining_trucks_count
        },
        c.UNLOAD_STATION: {
            c.PERFORMANCE: 0,
            c.EFFICIENCY: 0
        }
    }


def generate_truck_report(efficiency: list[int], performance: list[int]) -> pd:

    return pd.DataFrame({
        'Mining iterations': performance,
        'Average mining time': [round(efficiency[i] / performance[i], 2) for i in
                                range(len(efficiency))]
    },
        index=[f'Truck #{x}' for x in range(len(performance))])


def generate_unload_station_report(efficiency: int, performance : int) -> pd:

    return pd.DataFrame({
        'Unload iterations': performance,
        'Average unloading time': [round(efficiency / performance, 2) if performance else 0]
    },
        index=[f'Station #{0}'])


def calculate_and_report_statistics(data: dict, verbose: bool):
    # generate data frames
    mining_truck_df = generate_truck_report(efficiency=data[c.MINING_TRUCK][c.EFFICIENCY],
                                            performance=data[c.MINING_TRUCK][c.PERFORMANCE])
    unload_station_df = generate_unload_station_report(efficiency=data[c.UNLOAD_STATION][c.EFFICIENCY],
                                                       performance=data[c.UNLOAD_STATION][c.PERFORMANCE])
    # save reports to files
    mining_truck_df.to_csv(c.TRUCK_REPORT_FILE)
    unload_station_df.to_csv(c.UNLOAD_STATION_FILE)

    # print reports
    if verbose:
        print('\nMining trucks report')
        print(mining_truck_df)
        print('\nUnload stations report')
        print(unload_station_df)
