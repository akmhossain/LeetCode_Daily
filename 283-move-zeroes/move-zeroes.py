class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # if empty list return []
        # iterate non-zero-pointer to first index w/ value != 0
        # if value is not zero, swap with non-zero index, move non-zero index +1
        
        if not nums:
            return [] 

        non_zero = 0

        for i in range(len(nums)):
            if nums[i] != 0: # only swap non-zeroes to front
                nums[i], nums[non_zero] = nums[non_zero], nums[i]
                non_zero += 1

        return nums


        