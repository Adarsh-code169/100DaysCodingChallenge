class Solution:
    def rob_linear(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]

    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        return max(self.rob_linear(nums[1:]), self.rob_linear(nums[:-1]))

# # n = int(input())
# nums = list(map(int, input().split()))
# sol = Solution()
# print(sol.rob(nums))
