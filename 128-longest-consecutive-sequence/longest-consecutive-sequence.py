class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # set of all elements
        # find start of sequence: n-1 is not in set
        # record max

        s = set(nums)
        res = 0
        for i in s:
            if i - 1 not in s:
                curr_max = 0
                curr_num = i
                while curr_num in s:
                    curr_max += 1
                    curr_num += 1
                res = max(res, curr_max)
        
        return res
            