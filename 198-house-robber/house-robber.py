class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp + greedy algorithm (bottom up. tabulation)
        # dp contains the max amount of money so far

        if len(nums) == 1:
            return nums[0]
        
        dp = [0] * len(nums)
        dp[0] = nums[0] 
        dp[1] = max(nums[0], nums[1])

        for i in range(2,len(nums)):
            # set to max of robbing nums[i] vs not robbing nums[i]
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])

        return dp[-1]
