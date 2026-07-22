class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # stack is empty & closing bracket - false
        # opening bracket doesnt match closing (dict needed)
        # extra brakets at the end ()[

        if len(s) % 2 == 1:
            return False
        
        stk = []
        h = {'}':'{', ')':'(', ']':'['}
        
        for c in s:
            # if the char is closing bracket
            if c in h:
                if not stk:
                    return False
                if stk[-1] != h[c]:
                    return False
                else:
                    stk.pop()
            # if char is opening
            else:
                stk.append(c)
        
        return not stk

        




       