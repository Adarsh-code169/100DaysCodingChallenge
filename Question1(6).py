#Find The Highest Altitude

#There is a biker going on a road trip. The road trip consists of 
# n
# +
# 1
# n+1 points at different altitudes. The biker starts his trip on point 
# 0
# 0 with altitude equal 
# 0
# 0

# You are given an integer array gain of length 
# n
# n where 
# g
# a
# i
# n
# [
# i
# ]
# gain[i] is the net gain in altitude between points 
# i
# i​​​​​​ and 
# i
# +
# 1
# i+1 for all (0 <= i < n). Return the highest altitude of a point.
 
# Input
# User Task
# This is a function problem. You don't have to take any input. You are required to complete the function largestAltitude() which takes an array gain as parameters.

# Custom Input
# The first line will take an integer representing n.
# The second line will take n space-separated integers representing elements of the gain array.

# Constraints:
# 1 ≤ n ≤ 100
# -100 ≤ nums[i] ≤ 100
# Output
# Return the highest altitude of a point.
# Example
# Input:
# 5
# -5 1 5 0 -7
# Output:
# 1
# Explanation:
# The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.


#Code:
def largestAltitude(gain):
    res=[0]
    for i in range(0,len(gain)):
        temp=res[i]+gain[i]
        res.append(temp)
    return max(res)

