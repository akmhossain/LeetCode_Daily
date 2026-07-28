# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # if root == subroot, check if left and right also match
        def same(a, b):
            if not a and not b:
                return True
            if not a or not b:
                return False
            return a.val == b.val and same(a.left, b.left) and same(a.right, b.right)
        
        if not root:
            return False
        if same(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        