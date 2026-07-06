class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 != 0:
            return False
        
        h = {')':'(', '}':'{', ']':'['}
        stk = []

        for c in s:
            if c in h:
                if not stk or stk[-1] != h[c]:
                    return False
                stk.pop()
            else:
                stk.append(c)
        
        return not stk
                