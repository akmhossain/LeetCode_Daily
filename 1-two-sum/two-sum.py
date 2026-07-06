class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}
        for i in range(len(nums)):
            h[nums[i]] = i
        
        for i in range(len(nums)):
            if target - nums[i] in h and h[target-nums[i]] != i:
                return [i, h[target-nums[i]]]