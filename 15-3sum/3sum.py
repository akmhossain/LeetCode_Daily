class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort() # sort in ascending, gives us separation btwn negative and positive
        rt_list = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]: # skip duplicate results
                continue 
            if nums[i] > 0: # already exhausted negatives 
                break
            else: # find the other two numbers that complent negative to equal 0
                low = i + 1
                high = len(nums) -1
                while low < high:
                    total = nums[i] + nums[low] + nums[high]

                    if total == 0:
                        rt_list.append([nums[i], nums[low], nums[high]])

                        low += 1
                        high -= 1

                        # Skip duplicate second numbers
                        while low < high and nums[low] == nums[low - 1]:
                            low += 1

                        # Skip duplicate third numbers
                        while low < high and nums[high] == nums[high + 1]:
                            high -= 1

                    elif total < 0:
                        low += 1

                    else:
                        high -= 1
        
        return rt_list        



            

        