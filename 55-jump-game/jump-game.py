class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # start backwards and set a new goal once a space is able to be reached
        # if the goal eventually reaches 0 then true, otherwise false

        goal = len(nums) - 1

        for i in range(goal, -1, -1):
            max_jump = nums[i]
            if i + max_jump >= goal:
                goal = i
        
        return goal == 0

      
