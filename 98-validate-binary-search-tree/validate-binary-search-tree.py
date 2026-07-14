# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node,low,high):
            if not node:
                return True
            if node.val <= low or node.val >= high:
                return False    
            # left subtree must be smaller than node
            # right subtree must be larger than node
            return dfs(node.left,low,node.val) and dfs(node.right,node.val,high) 

        return dfs(root,float('-inf'),float('inf'))
