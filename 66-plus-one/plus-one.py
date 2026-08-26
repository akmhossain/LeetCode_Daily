class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # if digits[-1] == 0-8: digits[-1] += 1
        # if digits[-1] == 9 
        # ptr = -1, while 9 --> turn everything to 0, if at end then return [1] + digits
        
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        
        r = len(digits) - 1
        while digits[r] == 9 and r >= 0:
            digits[r] = 0
            r -= 1
        
        if r < 0:
            return [1,] + digits
        else: 
            digits[r] += 1
            return digits
        
        # 10599