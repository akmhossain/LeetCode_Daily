# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val 

        def dfs(node):
            nonlocal res # non local allows dfs to modify directly
            if not node:
                return 0

            leftMax = max(dfs(node.left), 0) # max against 0 to avoid negatives
            rightMax = max(dfs(node.right), 0)

            # maxSum with split(accounts for local peak)
            res = max(res, leftMax + rightMax + node.val)

            # choose larger side
            return node.val + max(leftMax, rightMax)
        
        dfs(root)
        return res
    
