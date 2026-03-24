import itertools

robots = ["R1", "R2", "R3", "R4"]
robot_capacity = {
    "R1": 3,
    "R2": 3,
    "R3": 3,
    "R4": 3
}

tasks = ["T1", "T2", "T3", "T4"]

cost_matrix = [
    [9, 2, 7, 8],
    [6, 4, 3, 7],
    [5, 8, 1, 8],
    [7, 6, 9, 4]
]

output = []

output.append("ROBOT LIST AND CAPACITIES\n")
for r in robots:
    output.append(f"{r} -> Capacity: {robot_capacity[r]}")

output.append("\nTASK LIST")
for t in tasks:
    output.append(t)

output.append("\nCOST/TIME MATRIX (Robot x Task)\n")

header = "     " + "  ".join(tasks)
output.append(header)

for i in range(len(robots)):
    row = robots[i] + "  " + "  ".join(str(x) for x in cost_matrix[i])
    output.append(row)

output.append("\nPOSSIBLE ALLOCATIONS CONSIDERED\n")

n = len(robots)
permutations = list(itertools.permutations(range(n)))

best_cost = float('inf')
best_assignment = None

for perm in permutations:
    total_cost = 0
    allocation = []

    for robot_index, task_index in enumerate(perm):
        cost = cost_matrix[robot_index][task_index]
        total_cost += cost
        allocation.append(f"{robots[robot_index]} -> {tasks[task_index]} ({cost})")

    output.append(" | ".join(allocation) + f"  Total Cost = {total_cost}")

    if total_cost < best_cost:
        best_cost = total_cost
        best_assignment = perm

output.append("\nFINAL OPTIMAL TASK ALLOCATION\n")

for robot_index, task_index in enumerate(best_assignment):
    output.append(
        f"{robots[robot_index]} assigned to {tasks[task_index]}  Cost = {cost_matrix[robot_index][task_index]}"
    )

output.append(f"\nTOTAL MINIMUM EXECUTION COST = {best_cost}")

output.append("\nALGORITHM USED: Assignment Problem (Brute-force for demonstration)")
output.append("Time Complexity: O(n!)")

file_name = "robot_task_allocation_output.txt"

with open(file_name, "w") as f:
    for line in output:
        print(line)
        f.write(line + "\n")

print(f"\nOutput saved to {file_name}")
