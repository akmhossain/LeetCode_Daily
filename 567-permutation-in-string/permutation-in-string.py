class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # a substring must be continuous, whereas a subsequence does not have to be continuous
        # s1 must be smaller and all its frequencies need to map to a substring(window) of s2
            # fixed sliding window on s2 

        if len(s1) > len(s2):
            return False

        # build map of s1
        h1 = {}
        for i in s1:
            h1[i] = h1.get(i, 0) + 1 

        # initial window 
        h2 = {}
        for i in range(len(s1)):
            if s2[i] in h2:
                h2[s2[i]] += 1
            else:
                h2[s2[i]] = 1

        if h1 == h2:
            return True
        
        l = 0
        for r in range(len(s1), len(s2)): # only need to loop remainder of s2, starting at s1
            h2[s2[r]] = h2.get(s2[r], 0) + 1 # advance right window by 1

            h2[s2[l]] -= 1 # advance window by one on left
            if h2[s2[l]] == 0:
                del h2[s2[l]]
            l += 1

            if h1 == h2: # check if frequency/permutation is present
                return True

        return False
        
