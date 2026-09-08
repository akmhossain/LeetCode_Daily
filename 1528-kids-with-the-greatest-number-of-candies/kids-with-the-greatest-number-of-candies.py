class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)
        diff = max_candy - extraCandies
        res = []
        for i in candies:
            if i >= diff:
                res.append(True)
            else:
                res.append(False)
        return res