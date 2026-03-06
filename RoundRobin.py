from dataclasses import dataclass, field
from collections import deque

@dataclass(order=True)
class Process:
    arrival_time: int
    burst_time: int
    process_id: str
    remaining_time: int = field(init=False)  # This field will be initialized in __post_init__

    def __post_init__(self):
        self.remaining_time = self.burst_time  # Initialize remaining time to burst time

def rr(processes, quantum):
    # Copy and sort processes by arrival
    all_process = sorted(processes, key=lambda p: (p.arrival_time, p.process_id))

    # list of ready processes
    ready_processes = deque()

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
        # take the next process from the ready queue
        the_ready_process = ready_processes.popleft()
        # simulate for quantum time or remaining time, whichever is smaller
        start = t
        time_slice = min(quantum, the_ready_process.remaining_time)
        end = start + time_slice

        scheduled_processes.append((the_ready_process, start, end))

        t= end
        the_ready_process.remaining_time -= time_slice

        while all_process and all_process[0].arrival_time <= t:
            ready_processes.append(all_process.pop(0))

        if the_ready_process.remaining_time == 0:
            completion_times[the_ready_process.process_id] = end
        else:
            ready_processes.append(the_ready_process)

    return scheduled_processes, completion_times

def tat(processes, completion_times):
    return {p.process_id: completion_times[p.process_id] - p.arrival_time for p in processes}

def att(tats):
    return sum(tats.values()) / len(tats) if tats else 0.0

def wt (processes, tats):
    return {p.process_id: tats[p.process_id] - p.burst_time for p in processes}

def rt (processes, completion_times):
    return {p.process_id: completion_times[p.process_id] - p.arrival_time - p.burst_time for p in processes}

example_processes = [
    Process(arrival_time=0, burst_time=2, process_id='p1'),
    Process(arrival_time=1, burst_time=1, process_id='p2'),
    Process(arrival_time=2, burst_time=8, process_id='p3'),
    Process(arrival_time=3, burst_time=4, process_id='p4'),
    Process(arrival_time=4, burst_time=5, process_id='p5'),
]

scheduled_processes, completion_times = rr(example_processes,2)

tats = tat(example_processes, completion_times)
average_tat = att(tats)
wt = wt(example_processes, tats)
rt = rt(example_processes, completion_times)

# Print results taken from CHATGPT 5.2
def print_sjf_results(scheduled_processes, completion_times, tats, average_tat, wts, average_wt, rts, average_rt):
    # Scheduled order (just process ids)
    order = [p.process_id for (p, start, end) in scheduled_processes]

    print("\nScheduled Order:")
    print(" -> ".join(order))

    # Timing graph
    print("\nTiming graph:")
    print(", ".join([f"{p.process_id} [{start}–{end}]" for (p, start, end) in scheduled_processes]))

    # Completion times
    print("\nCompletion Times:")
    for pid in sorted(completion_times.keys()):
        print(f"{pid}: {completion_times[pid]}")

    # Turnaround Times
    print("\nTurnaround Times (TAT):")
    for pid in sorted(tats.keys()):
        print(f"{pid}: {tats[pid]}")
    print(f"\nAverage Turnaround Time (ATT): {average_tat:.2f}")

    # Waiting Times
    print("\nWaiting Times (WT):")
    for pid in sorted(wts.keys()):
        print(f"{pid}: {wts[pid]}")
    print(f"\nAverage Waiting Time (AWT): {average_wt:.2f}")

    # Response Times
    print("\nResponse Times (RT):")
    for pid in sorted(rts.keys()):
        print(f"{pid}: {rts[pid]}")
    print(f"\nAverage Response Time (ART): {average_rt:.2f}")

print_sjf_results(scheduled_processes, completion_times, tats, average_tat, wt, att(wt), rt, att(rt))