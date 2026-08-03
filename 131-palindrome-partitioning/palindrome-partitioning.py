class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # use 2pointers to check is_palindrome
        def isPalindrome(s, start, end):
            if len(s) == 1:
                return True
            while start < end:
                if s[start] == s[end]:
                    start += 1
                    end -= 1
                else: 
                    return False
            return True
            
        res = []
        curr = []

        def dfs(i):
            if i == len(s): # base case
                res.append(curr.copy()) # copy 
                return
            for j in range(i,len(s)):
                if isPalindrome(s, i, j):
                    curr.append(s[i:j+1])
                    dfs(j+1)
                    curr.pop()
        
        dfs(0)
        return res
        
        

                

        