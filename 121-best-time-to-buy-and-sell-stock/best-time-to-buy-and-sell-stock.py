class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # keep track of the global min at each iteration
        # at each iteration update the result with curr - global minimum

        global_min, res = prices[0], -1

        for i in prices:
            global_min = min(global_min, i)
            res = max(res, i - global_min)
        
        return res

