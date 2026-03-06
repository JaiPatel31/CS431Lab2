CS431Lab2 — How to run the scheduler scripts

Summary

This repository contains three scheduling algorithm implementations in Python:

- `RoundRobin.py` — Round Robin (RR)
- `ShortestJobFirst.py` — Non-preemptive Shortest Job First (SJF)
- `ShortestRemainingTime.py` — Preemptive Shortest Remaining Time (SRT)

Each script is self-contained and runs an example workload when executed. The scripts print a scheduled order, a timing graph, completion times, turnaround/waiting/response times, and averages.

Prerequisites

- Windows (instructions use cmd.exe)
- Python 3.8 or newer installed and available on PATH (verify with: `python --version`)
- No external Python packages are required

Quick run (cmd.exe)

Open a Terminal in the project folder (for example: `C:\Users\GoldH\PycharmProjects\CS431Lab2`) and run one of the scripts:

python RoundRobin.py
python ShortestJobFirst.py
python ShortestRemainingTime.py

Each command will execute the example processes embedded at the bottom of the corresponding file and print results to the console.

What's printed

The scripts print several sections:

- Scheduled Order: the sequence of process ids in the schedule
- Timing graph: a compact timeline like `p1 [0–3], p2 [3–6]` showing run segments
- Completion Times: completion time for each process
- Turnaround Times (TAT) and Average Turnaround Time (ATT)
- Waiting Times (WT) and Average Waiting Time (AWT)
- Response Times (RT) and Average Response Time (ART)

How to run with custom inputs

There is no CLI argument parsing implemented in the scripts. To run with your own processes do one of the following:

1) Quick edit (recommended):
   - Open the script you want to run (for example `RoundRobin.py`) in an editor.
   - Find the `example_processes = [...]` list near the bottom of the file.
   - Replace or modify the `Process(...)` entries. Each `Process` takes three named fields:
     - `arrival_time` — integer arrival time
     - `burst_time` — integer CPU burst time
     - `process_id` — string id (e.g. `'p1'`)

   Example (in `RoundRobin.py`):
   Process(arrival_time=0, burst_time=2, process_id='p1')

   - For `RoundRobin.py` also change the quantum value in the call `rr(example_processes, 2)` to your desired time quantum.

   - Save and run `python RoundRobin.py` from cmd.exe.

2) Programmatic use (advanced):
   - You can import the `Process` dataclass and the scheduling function from a script in another Python file. Example:

   from ShortestJobFirst import Process, sjf
   procs = [Process(arrival_time=0, burst_time=3, process_id='p1'), ...]
   scheduled, completion = sjf(procs)

   - Then compute metrics with the helper functions present in the files (e.g. `tat`, `att`, `wt`, `rt`).

Notes and tips

- The example workloads are small; to simulate longer schedules, add more Process entries or larger burst times.
- If you receive `python` not found, make sure Python is installed and added to PATH, or run `py RoundRobin.py` if your system uses the Python launcher.
- The scripts are pure Python and do not modify files; they only print output to stdout.

Troubleshooting

- If you see SyntaxError or other exceptions, confirm you are using Python 3.8+.
- If you modify the scripts, run them after each change to verify behavior.
