
import argparse

def parse_cmd_options() -> argparse.ArgumentParser.parse_args:

    parser = argparse.ArgumentParser(prog='Helium-3',
                                     description='Simulation for a lunar Helium-3 space mining operation')
    parser.add_argument('-r',
                        '--truck',
                        type=int,
                        default=25,
                        help='Number of trucks dispatched for mining Helium-3')
    parser.add_argument('-s',
                        '--station',
                        type=int,
                        default=5,
                        help='Number of designated stations where trucks unload the mined Helium-3')
    parser.add_argument('-t',
                        '--time',
                        type=int,
                        default=72,
                        help='Mining time for simulation (in hours)')
    parser.add_argument('-v',
                        '--verbose',
                        action='store_true',
                        help='Verbose messaging while running simulation')

    args = parser.parse_args()

    if args.verbose:
        print('--- Simulation Details ---')
        print(f'Number of mining Trucks: {args.truck}')
        print(f'Number of unload Stations: {args.station}')
        print(f'Mining time: {args.time}')
        print('--- ---')

    return args
