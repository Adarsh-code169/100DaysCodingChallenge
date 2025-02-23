# #Implementing Bubble Sort


# Given a sequence of size N containing positive integers. You need to print the elements of sequence in increasing order using Bubble sort.
# Input
# User Task:
# This is a function problem. You don't have to take any input. You are required to complete the function bubbleSort() that takes an array seq as parameter.

# Custom Input
# The first line of the input denotes the number of test cases 'T'.
# The first line of the test case is the size of the array.
# The second line of the test case consists of array elements.

# Constraints:
# 1 ≤ T ≤ 100
# 1 ≤ N ≤ 1000
# 1 ≤ A[i] ≤ 1000

# Sum of N over all test cases doesn't exceed 5000.
# Output
# Return sorted list.
# Example
# Input:
# 2
# 5
# 4 1 3 9 7
# 10
# 10 9 8 7 6 5 4 3 2 1

# Output:
# 1 3 4 7 9
# 1 2 3 4 5 6 7 8 9 10

# Explanation:
# Testcase 1: 1 3 4 7 9 are in sorted form.
# Testcase 2: For the given input, 1 2 3 4 5 6 7 8 9 10 are in sorted form.



#Code:
def bubbleSort(seq):
    n = len(seq)
    for j in range(n):
        for i in range(n-j-1):
            if seq[i] > seq[i+1]:
                seq[i],seq[i+1] = seq[i+1],seq[i]

    return seq
