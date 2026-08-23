class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        m = {}
        
        for i,num in enumerate(nums):
            if target - num in m:
                return [i, m[target-nums[i]]]
            m[num] = i

        # 2 7 11 15, tar = 9
        {2:0, 7:1}