class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # base case: if p is none --> s is empty: return true, else false
        # helper funcitons for * and .
        # if p[0] is letter: match with s + recursion, else false
        # if p[0] is .: call the helper:
          # helper: 
        
        # base
        if not p:
            return not s
        if not s: # handles s = "", p = "a*b*b*"
            if len(p) > 1 and p[1] == "*":
                return self.isMatch(s, p[2:])
            return not p
        
        # look ahead for *
        if len(p) > 1 and p[1] == '*': 
            # if zero elements match preceding, go to next iteration
            # while s[curr] == preceding: slice the first element
            if p[0] != '.' and p[0] != s[0]:
                return self.isMatch(s, p[2:])

            curr = 0
            while (curr < len(s)) and (p[0] == "." or s[curr] == p[0]):
                if self.isMatch(s[curr:], p[2:]):
                    return True # string matches pattern completely
                curr += 1 
            
            return self.isMatch(s[curr:], p[2:])

        if p[0].isalpha():
            if p[0] == s[0]:
                return self.isMatch(s[1:], p[1:])
            else:
                return False
        
        if p[0] == ".":
            return self.isMatch(s[1:], p[1:])

    # s = bba, p = b*ba
        
        


        
        
        
        