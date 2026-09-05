class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # seen = [0] * (len(nums) + 1) # each index represents num
        # for i in nums:
        #     seen[i] = 1
        
        # for i in range(len(seen)):
        #     if seen[i] == 0:
        #         return i

        total = sum([i for i in (range(len(nums) + 1))])
        return total - sum(nums)
        