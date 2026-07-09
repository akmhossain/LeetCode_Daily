# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        # no tree or all nodes visited: return false
        # solution: recursively check left/right and subtract from target
          # if targetSum is 0 and node is leaf(no l/r): return True

        # edge case
        if not root:
            return False 

        # check if leaf and target reached
        targetSum = targetSum - root.val 
        if targetSum == 0 and (not root.right and not root.left):
            return True
        
        # dfs 
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
        
        
        