class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]

        dp = triangle[-1][:] # bottom --> up, add min to each index
        
        for row in range(len(triangle)-2, -1, -1):
            for i in range(len(triangle[row])):
                dp[i] = triangle[row][i] + min(dp[i], dp[i+1])
        
        return dp[0]
