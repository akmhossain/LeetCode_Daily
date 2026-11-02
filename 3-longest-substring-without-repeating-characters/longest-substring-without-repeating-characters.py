class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window: keep a max_res variable
        # l, r = 0, 1
        # dynamic window: while r < len list
            # need to keep a set of current seen
            # if l == r then 

        if not s:
            return 0
        
        l,r = 0,0
        curr_seen = set()
        res = -1

        while r < len(s):
            while s[r] in curr_seen: # shrink window until the first of the duplicates (l) is gone
                curr_seen.remove(s[l])
                l += 1
            
            curr_seen.add(s[r]) # increase window otherwise
            res = max(res, r - l + 1)
            r += 1

        return res

        # abcbc