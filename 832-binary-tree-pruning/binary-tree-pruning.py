# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # post-order solution: deletion happens as recursion unwinds
        # l-r-root
        if not root:
            return None

        # change the actual trees to the result of the call 
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        
        if root.val == 0 and (not root.left and not root.right): # delete root if 0 w/ no children
            return None
        
        return root

            