# Round Robin Scheduling Algorithm
def round_robin(processes, burst_time, quantum):
    n = len(processes)
    remaining_burst_time = burst_time[:]
    waiting_time = [0] * n
    turnaround_time = [0] * n
    time = 0

    while True:
        done = True
        for i in range(n):
            if remaining_burst_time[i] > 0:
                done = False
                if remaining_burst_time[i] > quantum:
                    time += quantum
                    remaining_burst_time[i] -= quantum
                else:
                    time += remaining_burst_time[i]
                    waiting_time[i] = time - burst_time[i]
                    remaining_burst_time[i] = 0
        if done:
            break

    for i in range(n):
        turnaround_time[i] = burst_time[i] + waiting_time[i]

    return waiting_time, turnaround_time


# Example usage
if __name__ == "__main__":
    processes = [1, 2, 3]  # Process IDs
    burst_time = [10, 5, 8]  # Burst times for each process
    quantum = 2  # Time quantum

    waiting_time, turnaround_time = round_robin(processes, burst_time, quantum)

    print("Processes    Burst Time    Waiting Time    Turnaround Time")
    for i in range(len(processes)):
        print(f"    {processes[i]}             {burst_time[i]}             {waiting_time[i]}                {turnaround_time[i]}")

    print(f"\nAverage Waiting Time: {sum(waiting_time) / len(processes):.2f}")
    print(f"Average Turnaround Time: {sum(turnaround_time) / len(processes):.2f}")