class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        L=0
        min_length=float('inf')
        current_sum=0

        for R in range(len(nums)):
            current_sum+=nums[R]
            while current_sum>=target:
                min_length=min(min_length,R-L+1)
                current_sum-=nums[L]
                L+=1
        return 0 if min_length== float('inf') else min_length
                

        