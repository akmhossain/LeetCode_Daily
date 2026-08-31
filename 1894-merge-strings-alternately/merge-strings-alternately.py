class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # two pointer approach
        # if one pointer runs out, find the difference of length and append

        if len(word2) < len(word1):
            smaller = len(word2)
            greater_word = word1
        else:
            smaller = len(word1)
            greater_word = word2
        
        res = ""
        
        for i in range(smaller):
            res += word1[i] + word2[i]
        
        res += greater_word[smaller:]

        return res
