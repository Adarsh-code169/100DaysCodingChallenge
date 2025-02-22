# #Minimum Size Subarray Sum K
#
#
# Input
# 7 19
# 5 2 5 5 3 1 5
# Output
# 5
# Explanation
# Subarray from index 3 to 7 is the subarray with minimum possible length whose subarray sum is greater than or equal to 19.
# 5+5+3+1+5=19


#Code:
def minSubArray(arr, k):
    n = len(arr)
    left = 0
    current_sum = 0
    min_length = float('inf')

    for right in range(n):
        current_sum += arr[right]

        while current_sum >= k:
            min_length = min(min_length, right - left + 1)
            current_sum -= arr[left]
            left += 1

    return min_length if min_length != float('inf') else 0
