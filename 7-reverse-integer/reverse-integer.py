class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x < 0 else 1
        x = abs(x)
        res = 0
        
        while x > 0:
            res = (res * 10) + (x % 10)
            x //= 10
            
        res *= sign
        
        # 32-bit signed integer overflow check
        if res < -2**31 or res > 2**31 - 1:
            return 0
            
        return res