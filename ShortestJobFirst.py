# It is a non-preemptive algorithm. It usese the total time required by a process to
# execute as the basis for scheduling.
# The process with the smallest total time to completion is selected for execution next
from dataclasses import dataclass
from typing import List, Dict, Tuple

# Create a process class to hold some PCB fields
@dataclass(order=True)
class Process:
    arrival_time: int
    burst_time: int
    process_id: str

def sjf(processes):
    # Copy and sort processes by arrival
    all_process = sorted(processes, key=lambda p: (p.arrival_time, p.process_id))

    # list of ready processes
    ready_processes = []

    # list of scheduled processes
    scheduled_processes = []

    # completion time of processes
    completion_times = {}

    # current time
    t = 0

    #Loop until there are no processes left to run
    while all_process or ready_processes:
        # Admit all processes that are ready
        # by checking if their (arrival time <= current time)
        while all_process and all_process[0].arrival_time <= t:
            ready_processes.append(all_process.pop(0))
        # Check if CPU would ide (no ready process at the current time)
        if not ready_processes:
            # Jump time to next process arrival time
            t = all_process[0].arrival_time
            continue
        # choose the next process to run
        ready_processes.sort(key=lambda p: (p.burst_time, p.arrival_time))

        #take the process with the shortest burst time
        the_ready_process = ready_processes.pop(0)

        # simulate
        start = t
        end = start + the_ready_process.burst_time
        scheduled_processes.append((the_ready_process, start, end))
        completion_times[the_ready_process.process_id] = end

        t = end


    return scheduled_processes, completion_times
def tat(example_processes, completion_times):
    return {p.process_id: completion_times[p.process_id] - p.arrival_time for p in example_processes}

def att(tats):
    return (sum(tats.values()) / len(tats)) if tats else 0.0

example_processes = [
    Process(arrival_time=0, burst_time=6, process_id='p1'),
    Process(arrival_time=1, burst_time=3, process_id='p2'),
    Process(arrival_time=3, burst_time=2, process_id='p3'),
]

scheduled_processes, completion_times = sjf(example_processes)
tat = tat(example_processes, completion_times)
att = att(tat)
print(scheduled_processes)
print(completion_times)
print(tat)
print(att)