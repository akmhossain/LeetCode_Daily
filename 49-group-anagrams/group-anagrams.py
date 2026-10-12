class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # brute force
        # create result list
        # function to get alphebetically sorted words

        h = {} # sorted key:list of corresponding words
        for i in strs:
            sorted_str = "".join(sorted(i))
            if sorted_str in h:
                h[sorted_str].append(i)
            else:
                h[sorted_str] = [i]
        
        return list(h.values())