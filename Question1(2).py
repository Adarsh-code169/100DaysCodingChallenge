#100 Days of Code Completed?


# The 100 Days of Code challenge runs at Newton School of Technology (NST). Each day, two problems are released together: one in the morning and one in the evening. To win the contest, participants need to solve at least one problem each day for 100 days.
# You are given two arrays:
#
# • array1: Represents whether the first problem of the day has been solved (1 if solved, 0 if not solved).
#
# • array2: Represents whether the second problem of the day has been solved (1 if solved, 0 if not solved).
#
# The size of both arrays is 100, corresponding to 100 days of the contest. Your task is to determine if the participant has successfully completed the contest by solving at least one problem each day for all 100 days.
#
# Input
# The first line contains 100 space-separated integers array1, representing the status of the first problem (1 for solved, 0 for not solved) for each day of the contest.
# The second line contains 100 space-separated integers array2, representing the status of the second problem (1 for solved, 0 for not solved) for each day of the contest.
# Output
# Print True if the participant has successfully completed the challenge (i.e., at least one problem is solved each day for all 100 days) else Print False.
# Example
# Sample Input:
# 0 0 1 1 0 1 1 0 0 1 1 0 1 1 1 0 0 1 1 1 0 1 0 1 1 1 0 1 1 0 1 0 1 1 0 1 1 0 1 1 0 1 0 1 0 1 1 1 0 0 1 1 0 1 1 0 1 0 1 1 0 0 1 0 1 1 1 1 0 0 1 0 1 1 1 0 1 0 1 1 0 1 0 1 1 0 1 1 1 1 0 0 1 1 0 1 0 1 1 0
# 0 1 0 0 1 0 1 1 0 0 1 1 0 0 1 1 1 0 0 1 1 0 1 0 0 1 0 1 0 1 1 0 0 1 1 1 0 0 0 1 0 1 1 1 1 1 0 1 0 0 1 1 1 1 1 0 1 0 0 1 0 1 0 1 1 1 1 0 0 0 1 1 0 1 1 1 1 0 1 0 0 1 1 1 1 1 0 1 0 0 1 1 0 0 1 0 1 0 1 0
#
# Sample Output:
# False
#
# Explanation:
# The participant was eliminated since the participant did not solve any problem on Day 0.



#Code:
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
valid=True
for i in range(100):
    if arr1[i]==1 or arr2[i]==1:
        pass
    else:
        valid=False
        break
print(valid)
