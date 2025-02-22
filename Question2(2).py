# #Kth largest element in an Array
#
#
# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
#
# Input
# User Task
# This is a function problem. You don't have to take any input. You are required to complete the function findKthLargest() which takes an array nums  and integer k as parameters.
#
# Custom Input
# The first line will take two space-separated integers representing n and k.
# The second line will take n space-separated integers representing elements of the nums array.
#
# Constraints:
# 1 ≤ k ≤ nums.length ≤ 105
# -104 ≤ nums[i] ≤ 104
# Output
# Return the Kth largest element in the array.
# Example
# Input:
# 3 3
# 3 2 1
# Output:
# 1
# Explanation:
# 3 is 1st largest, 2 is 2nd largest and 1 is 3rd largest(kth) so 1 is the kth largest element in the array.
#
# Input:
# 6 2
# 3 2 1 5 6 4
# Output:
# 5
# Explanation:
# 6 is 1st largest and 5 is 3rd largest(kth) so 5 is the kth largest element in the array.


#Code:
def findKthLargest(nums, k):
    temp=sorted(nums,reverse=True)
    return temp[k-1]
