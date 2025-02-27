#Factorial using Recursion

# The Factorial of a number n, can be written as

# Fac(n)=n∗Fac(n−1), with Fac(0)=1

# Write a program that calculates the factorial of a given non-negative integer n using recursion. The factorial of a number n is defined as the product of all integers from 1 to n.

# You have to take input and then call the funtion to print the output.
 
# Input
# The only line of input contains integer n, representing the number for which the factorial needs to be calculated.

# Constraints
# 0 <= n <= 10
# Output
# A single integer, representing the factorial of n.
# Example
# Input:
# 5
# Output:
# 120
# Explanation:
# The input integer n is 5. We need to calculate the factorial of 5.
# Factorial of 5 = 5 * 4 * 3 * 2 * 1 = 120

# Input:
# 7
# Output:
# 5040
# Explanation:
# The input integer n is 7. We need to calculate the factorial of 7.
# Factorial of 7 is calculated as: 7!=7×6×5×4×3×2×1=5040
# Thus, the output is 5040.






#Code:
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

n = int(input())
print(factorial(n))
