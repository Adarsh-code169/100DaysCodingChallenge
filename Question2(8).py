# #Subarray Sum Divisible by K


# Given an integer array A of size N and an integer K. Find the number of non- empty subarrays that have a sum divisible by K. A subarray is a contiguous part of an array.
# Input
# First line contains two integers N and K.
# Next line contains N space separated integers denoting elements of array.

# Constraints
# 1 <= K, N <= 10^4
# 0 <= Ai <= 10^4
# Output
# Print the number of non- empty subarrays that have a sum divisible by K.
# Example
# Sample Input 1:
# 5 2
# 4 5 0 2 3

# Output
# 6

# Explanation:
# All possible subarray sums are:
# Subarray with size =1  = {4, 5, 0, 2, 3}
# Subarray with size =2  = {9, 5, 2, 5}
# Subarray with size =3  = {9, 7, 5}
# Subarray with size =4  = {11, 10}
# Subarray with size =5  = {14}
# Numbers divisible by 2 are {4, 0, 2, 2, 10, 14}



#Code:
n, k = map(int, input().split())
p = list(map(int, input().split()))
count = 0
pre = 0
freq = {0: 1}
for i in range(len(p)):
    pre += p[i]
    rem = pre % k
    if rem < 0:
        rem += k
    if rem in freq:
        count += freq[rem]
    if rem in freq:
        freq[rem] += 1
    else:
        freq[rem] = 1
print(count)
