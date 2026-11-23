class Solution:
    def longestSubsequence(self, arr: list[int], difference: int) -> int:
        # cannot change order - no sorting
        # can take any sequence of elements 
        # use dp with hashmap (index_val:longest length at idx)

        dp = {}
        ans = 0

        for x in arr:
            dp[x] = dp.get(x - difference,0) + 1
            if dp[x] > ans:
                ans = dp[x]

        return ans