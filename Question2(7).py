# #Running Sum of 1D Array

# User Task
# This is a function problem. You don't have to take any input. You are required to complete the function runningSum() which takes an array nums as parameters.

# Custom Input
# The first line will take an integer representing n.
# The second line will take n space-separated integers representing elements of the nums array.

# Constraints:
# 1 ≤ n ≤ 2 * 103
# -106 ≤ nums[i] ≤ 106
# Output
# Return an array containing the running sum of nums.
# Example
# Input:
# 4
# 1 2 3 4
# Output:
# 1 3 6 10
# Explanation:
# The running sum is calculated as follows: [1, 1+2, 1+2+3, 1+2+3+4].


#Code:
def runningSum(nums):
    n=len(nums)
    prefix=[0]*n
    prefix[0]=nums[0]

    for i in range(1,n):
        prefix[i]=prefix[i-1]+nums[i]

    return prefix
