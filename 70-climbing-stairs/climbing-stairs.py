class Solution:
    def climbStairs(self, n: int) -> int:
        # bottom up approach
        # at 1 theres 1 way, at 2 theres (1) + 1 new way, at 3 theres 1 more way than 2
        # pattern: fib, each step is the sum of the prev 2 steps

        if n < 3:
            return n
        
        l,r = 1,2
        for i in range(3,n+1):
            l,r = r,l+r
     
        return r