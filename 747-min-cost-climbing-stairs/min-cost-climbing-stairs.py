class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # if len == 2, return min(cost[0], cost[1])
        # if len == 3, return min(cost[0] + cost[2], cost[1])
        # if len == 4, return min

        dp = [0] * (len(cost) + 1) # dp[i] is the min to climb to top from i

        for i in range(2,len(cost)+1):
            dp[i] = min(cost[i-1] + dp[i-1], cost[i-2] + dp[i-2])
        
        return dp[-1]

