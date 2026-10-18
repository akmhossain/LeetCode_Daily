class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 2pointers - front back string
        # check if l,r are non-letters
            # if so increment the pointer
            # check the lower case versions of l and r are same
        
        l,r = 0,len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum(): # l < r for cases all str non alpha-num
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
        
        return True

        # edge cases: "0P" 