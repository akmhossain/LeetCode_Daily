class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # use hashmap for quick storage and lookup
        # loop through list
            # if the [target - curr val] is in h then return the indices of curr/val
        
        h = {} # store val:index pair

        for idx,val in enumerate(nums):
            if target - val in h:
                return [h[target-val],idx]
            h[val] = idx

