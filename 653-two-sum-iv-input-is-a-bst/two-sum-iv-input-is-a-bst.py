# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: bool
        """
        # recursively build hashset 
        h = set()
        def dfs(node):
            if not node:
                return False # reached end of tree with no match
            if k - node.val in h:
                return True
            h.add(node.val)
            return dfs(node.left) or dfs(node.right)
        return dfs(root)