# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # max path has to be the deepest leaf in the left side + deepest leaf on the right side
        self.res = 0

        def height(node):
            if not node:
                return 0
            l,r = height(node.left), height(node.right) # must finish executing before next line
            self.res = max(self.res, l + r) # runs as call stack unwinds after hitting base case
            return 1 + max(l,r)
        
        height(root)
        return self.res
            