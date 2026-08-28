class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # if len == 2, return min(cost[0], cost[1])
        # if len == 3, return min(cost[0] + cost[2], cost[1])
        # if len == 4, return min
        # start backwards with dp array, cost at the end is 0

        dp = [0] * (len(cost) + 2) # dp[i] is the min to climb to top from i

        for i in range(len(cost)-1, -1, -1):
            dp[i] = cost[i] + min(dp[i+1], dp[i+2])
        
        return min(dp[0], dp[1])

