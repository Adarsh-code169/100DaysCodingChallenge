# # Little Alice and Numbers

# Little Alice has recently started studying multiples of 5, and today he is particularly fascinated by numbers divisible by 5. He has a collection of queries where each query provides a range of indices [l, r] in an array of integers arr and asks him to find how many integers in that range are divisible by 5.

# Joe wants to automate this process, so he can quickly answer any number of queries without doing repetitive manual calculations. Can you help him?

# Task:
# You are given an array arr and Q queries. Each query consists of two integers l and r representing a range [l, r] in the array arr. Your task is to determine how many integers in this range of the array arr are divisible by 5.
# Write a program that solves the problem for multiple queries, and outputs the result for each query.

# Note:
# Endpoints of the range are inclusive i.e indices l and r are included in range [l, r].

# Input
# The first line of input contains a single integer N, representing the number of elements in the array.
# The second line contains N space-separated integers.
# The third line contains a single integer Q (1 ≤ Q ≤ 1000) — the number of queries.
# Then, Q lines follow. Each line contains two space separated integers l and r (0 ≤ l ≤ r < 104) representing the range [l, r].

# Constraints
# 1 <= N <= 104
# 1 ≤ Q ≤ 1000 (Number of queries)
# 0 <= element of list <= 105
# 0 ≤ l ≤ r < N(Range limits)

# Optional Constraints
# 1 <= N <= 104
# 1 ≤ Q ≤ 105 (Number of queries)
# 0 <= element of list <= 105
# 0 ≤ l ≤ r < N(Range limits)
# Output
# For each query, print the number of integers in the range [l, r] of the array arr that are divisible by 5.
# Example
# Input
# 10
# 1 4 5 2 6 5 0 15 15 5
# 3
# 0 9
# 1 4
# 3 9

# Output
# 6
# 1
# 5

# Explanation
# Query 1 (l = 0, r = 9):
# The integers divisible by 5 in the range [0, 9] are: 5, 5, 0, 15, 15, 5.
# Therefore, the answer is 6.

# Query 2 (l = 1, r = 4):
# The integers divisible by 5 in the range [1, 4] are: 5.
# Therefore, the answer is 1.

# Query 3 (l = 3, r = 9):
# The integers divisible by 5 in the range [3, 9] are: 5, 0, 15, 15, 5.
# Therefore, the answer is 5.




#Code:
# Your code here
def count_multiples_of_5(arr, queries):
    prefix_count = [0] * (len(arr) + 1)
    
    for i in range(len(arr)):
        prefix_count[i + 1] = prefix_count[i] + (1 if arr[i] % 5 == 0 else 0)
    
    results = []
    for l, r in queries:
        results.append(prefix_count[r + 1] - prefix_count[l])
    
    return results

n = int(input())
arr = list(map(int, input().split()))
q = int(input())
queries = [tuple(map(int, input().split())) for _ in range(q)]

for res in count_multiples_of_5(arr, queries):
    print(res)
