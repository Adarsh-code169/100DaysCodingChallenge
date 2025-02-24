# #Find The Diagonal Sum

# # Given a square matrix of order 
# # N∗N
# # N∗N, your task is to find the sum of the elements of the primary and secondary diagonal of the matrix.
# # The image given below illustrates the primary and secondary diagonal:
# Note: The element common to both the diagonals should only be counted once. For the above-shown matrix, the common element 5 will only be added once, and the overall sum will be 1 + 3 + 5 + 7 + 9 = 25.
# Input
# User Task
# You don't need to read inputs or print anything. Complete the function calculate_diagonal_sum(matrix) that takes the matrix as input parameter.

# Custom Input
# The first line contains a single integer 
# N
# N, representing the order of matrix.
# Each of the following 
# N
# N lines contain, 
# N
# N space separated integers, representing the elements of the N * N matrix.


# Output
# Return the sum of the elements of the primary and secondary diagonals.
# Example
# Sample Input 1
# 3
# 1 2 3
# 4 5 6
# 7 8 9
# Sample Output 1
# 25
# Sample Explanation 1
# Elements of the primary diagonal are 1, 5, and 9. And the elements of the secondary diagonal are 3, 5, and 7. Thus the sum of elements of both the diagonals will be 1 + 5 + 9 + 3 + 7 = 25 (considering the common element 5 only once).




#Code:
def calculate_diagonal_sum(matrix):
    sum=0
    for i in range(len(matrix)):
        sum+=matrix[i][i]+matrix[i][len(matrix)-1-i]
    return sum-(matrix[len(matrix)//2][len(matrix)//2] if N%2 else 0)
