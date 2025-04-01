class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {0: 1}
        for num in nums:
            new_dp = {}
            for summ in dp:
                new_dp[summ + num] = new_dp.get(summ + num, 0) + dp[summ]
                new_dp[summ - num] = new_dp.get(summ - num, 0) + dp[summ]
            dp = new_dp
        return dp.get(target, 0)