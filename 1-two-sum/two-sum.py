class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}
        
        for i,num in enumerate(nums):
            if target - num in h:
                return [i, h[target-nums[i]]]
            h[num] = i
