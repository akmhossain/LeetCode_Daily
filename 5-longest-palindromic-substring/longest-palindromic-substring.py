class Solution:
    def longestPalindrome(self, s: str) -> str:
        # check palindrome from the center
        if len(s) == 1:
            return s

        max_string = ""
        for i in range(len(s)):
            # odd center checks, l/r is one l/r to center
            l,r = i - 1, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if  r - l - 1 > len(max_string):
                max_string = s[l+1:r]

            # even center checks, l/r is center
            l,r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if  r - l - 1 > len(max_string):
                max_string = s[l+1:r]

        return max_string