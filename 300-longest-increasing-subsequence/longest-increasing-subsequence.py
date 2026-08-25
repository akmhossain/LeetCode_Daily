class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # maintain a dp array where each idx represents the max subseq upto that point including idx
        # recursion backwards starting from last idx
        # only increment with last LIS call if curr value is less

        n = len(nums)
        LIS = [1] * n # each idx stores the LIS at that idx in nums

        for i in range(n-1, -1, -1):
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j]) # uses cached LIS from idx already visited
        
        return max(LIS)
           
        # [10, 2, 3, 5, 7, 6, 7, 8]