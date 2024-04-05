def fcfs_scheduling(processes):
    current_time = 0  # setting the currect start time of the CPU
    header = ("| Process | Arrival Time | Service Time | Finish Time | Turnaround Time | Normalized Turnaround Time |")
    print(header)
    print("-" * len(header))
    process = ["", "A", "B", "C", "D", "E", "F", "G"]

    total_turnaround_time = 0
    total_normalized_turnaround_time = 0

    for i, (arrival_time, service_time) in enumerate(processes, start=1):
        if current_time < arrival_time:
            current_time = arrival_time
        # The Finish time is current time plus service time
        finish_time = current_time + service_time
        # The Turnaround time is finish time subtract arrival time
        turnaround_time = finish_time - arrival_time
        # The Normalized Turnaround Time is turnaround time divided by service time
        normalized_turnaround_time = turnaround_time / service_time
        # These are for the averages
        total_turnaround_time += turnaround_time
        total_normalized_turnaround_time += normalized_turnaround_time

        print(f"|{process[i]:^9}| {arrival_time:>12} | {service_time:>11}  | {finish_time:>11} | {turnaround_time:>14}  | {normalized_turnaround_time:>26.2f} |")
        current_time = finish_time
    #The average turnaround time is the total turnaround time divided by the amount of processes
    average_turnaround_time = total_turnaround_time / len(processes)
    #The average normalized turnaround time is the total normalized turnaround time divided by the amount of processes
    average_normalized_turnaround_time = total_normalized_turnaround_time / len(processes)
    print("-" * len(header))

    print(f"Average Turnaround Time: {average_turnaround_time:.2f}")
    print(f"Average Normalized Turnaround Time: {average_normalized_turnaround_time:.2f}")


processes = [(0, 3), 
             (2, 6), 
             (5, 5), 
             (6, 3), 
             (8, 6), 
             (9, 2), 
             (10, 6)]

print("\n")
fcfs_scheduling(processes)
print("\n")

