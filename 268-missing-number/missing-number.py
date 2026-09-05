class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # seen = [0] * (len(nums) + 1) # each index represents num
        # for i in nums:
        #     seen[i] = 1
        
        # for i in range(len(seen)):
        #     if seen[i] == 0:
        #         return i

        missing = 0
        while missing < len(nums):
            if missing in nums:
                missing += 1
            else:
                return missing
        
        return missing 