class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy low --> sell high
        # at each update the minimum, res(max(res, curr-min)) 

        min_price, res = prices[0], -1

        for i in prices:
            min_price = min(i, min_price)
            res = max(res, i - min_price) 
        
        return res
