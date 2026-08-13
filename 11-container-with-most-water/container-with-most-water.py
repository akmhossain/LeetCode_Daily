class Solution:
    def maxArea(self, height: List[int]) -> int:
        # l,r pointers, loop while l < r
        # choose the bigger bar 
        l,r = 0,len(height)-1
        res = 0
        while l < r+1:
            area = min(height[l], height[r]) * (r-l)
            res = max(res, area)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        
        return res