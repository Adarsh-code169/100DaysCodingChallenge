class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, float('-inf'), float('-inf')]
        for num in nums:
            temp = dp[:]
            for i in range(3):
                dp[(i + num) % 3] = max(dp[(i + num) % 3], temp[i] + num)
        return dp[0]
            