# Helium-3

## Simulation for a lunar Helium-3 space mining operation.

### Objective:
You are tasked with developing a simulation for a lunar Helium-3 space mining operation. This
simulation will manage and track the efficiency of mining trucks and unload stations over a
continuous 72-hour operation.

### Key Components:
* Mining Trucks: These vehicles perform the actual mining tasks.
* Mining Sites: Locations on the moon where the trucks extract Helium-3. Assume an infinite
number of sites, ensuring trucks always have access to mine without waiting.
* Mining Unload Stations: Designated stations where trucks unload the mined Helium-3. Each
station can handle one truck at a time.

### Operation Details:
* There are (n) mining trucks and (m) mining unload stations.
* Mining trucks can spend a random duration between 1 to 5 hours mining at the sites.
* It takes a mining truck 30 minutes to travel between a mining site and an unload station.
  * Assume all trucks are empty at a mining site when the simulation starts.
* Unloading the mined Helium-3 at a station takes 5 minutes.
* Trucks are assigned to the first available unload station. If all stations are occupied, trucks
queue at the station with the shortest wait time and remain in their chosen queue.

### Simulation Requirements:
* The simulation must be configurable to accommodate various numbers of mining trucks (n)
and unload stations (m).
* Calculate and report statistics for the performance and efficiency of each mining truck and
unload station.
* The simulation represents 72 hours of non-stop mining and must execute faster than
real-time to provide timely analysis.

### Language and programming paradigms:
Please implement this project in Python. Please leverage OOP where it is appropriate.


## Requirements

- [Python](https://www.python.org/downloads/) ~= 3.13.1


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies.

```commandline
pip install -r requirements.txt
```


## Usage

Run simulation.

By default, simulator runs with:
- 25 mining trucks
- 5 unloading stations
- 72 hours of simulation

Simulation report will be created in "Reports" directory.

```commandline
python run_simulation.py
```


## Parameters:

* Number of trucks dispatched for mining Helium-3
```commandline
[ -r | --truck ] 
```

* Number of designated stations where trucks unload the mined Helium-3
```commandline
[ -s | --station ]
```

* Mining time for simulation [hours]
```commandline
[ -t | --time ]
```

* Verbose messaging while running simulation
```commandline
[ -v | --verbose ]
```

example 
```commandline
python run_simulation.py -r 37 -s 3 -t 10 -v
```
