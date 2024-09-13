# arr = [
#     ['a', 2, 100], 
#     ['b', 2, 20], 
#     ['c', 1, 40], 
#     ['d', 3, 35], 
#     ['e', 1, 25]
# ]

# print("Following is the maximum profit sequence of jobs:")

# # Length of the array
# n = len(arr)

# # Number of time slots available
# t = 3

# # Sort all jobs according to decreasing order of profit
# for i in range(n):  # i starts from 0
#     for j in range(n - 1 - i):
#         if arr[j][2] < arr[j + 1][2]:
#             arr[j], arr[j + 1] = arr[j + 1], arr[j]

# # To keep track of free time slots
# result = [False] * t

# # To store the sequence of jobs
# job = ['-1'] * t

# # Variable to store total profit
# total_profit = 0

# # Iterate through all given jobs
# for i in range(len(arr)):

#     # Find a free slot for this job
#     # (Note that we start from the last possible slot)
#     for j in range(min(t - 1, arr[i][1] - 1), -1, -1):

#         # Free slot found
#         if result[j] is False:
#             result[j] = True
#             job[j] = arr[i][0]
#             total_profit += arr[i][2]  # Add the profit of this job
#             break

# # Print the sequence of jobs
# print(job)

# # Print the total profit
# print("Total profit:", total_profit)

arr = [
    ['a', 2, 100], 
    ['b', 2, 20], 
    ['c', 1, 40], 
    ['d', 3, 35], 
    ['e', 1, 25]
]

print("Following is the maximum profit sequence of jobs:")

# Number of time slots available
t = 3

# Sort all jobs according to decreasing order of profit using built-in sorted()
arr = sorted(arr, key=lambda x: x[2], reverse=True)

# To keep track of free time slots
result = [False] * t

# To store the sequence of jobs
job = ['-1'] * t

# Variable to store total profit
total_profit = 0

# Iterate through all given jobs
for i in range(len(arr)):

    # Find a free slot for this job
    # (Note that we start from the last possible slot)
    for j in range(min(t - 1, arr[i][1] - 1), -1, -1):

        # Free slot found
        if result[j] is False:
            result[j] = True
            job[j] = arr[i][0]
            total_profit += arr[i][2]  # Add the profit of this job
            break

# Print the sequence of jobs
print(job)

# Print the total profit
print("Total profit:", total_profit)
