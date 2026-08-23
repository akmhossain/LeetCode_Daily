class Solution:
    def fib(self, n: int) -> int:
        # tabulation - bottom up array
        # F(n) = F(n-1) + F(n-2)
        if n == 0:
            return 0
            
        dp = [0,1]
        for i in range(2,n+1):
            dp.append(dp[i-1] + dp[i-2])
        return dp[-1]