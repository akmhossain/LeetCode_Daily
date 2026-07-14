# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        # PATH definition(from claude):
        # A path in a tree, in the general sense used across these problems, is: a sequence of nodes where each consecutive pair is connected by an edge, and no node is repeated.
        # In simpler terms a path is either a straight line, or a line with a peak (example 2)

        # if not root, return 0
        # set res = 0
        # dfs on left/right, reset if no match, +1 if match 

        res = 0 # initial result
        
        def dfs(node):
            nonlocal res # uses res from outside the function, to avoid res = 0 every call
            if not node:
                return 0 # base case

            L = dfs(node.left)
            R = dfs(node.right)

            # at each node update logic
            if node.left and node.left.val == node.val:
                L += 1
            else:
                L = 0
            
            if node.right and node.right.val == node.val:
                R += 1
            else:
                R = 0
            
            # to scan for any peaks, at every node add L + R
            res = max(res, L + R)

            # at each parent node choose the subtree with greater univariate length
            return max(L,R)
        
        dfs(root)
        return res
            


        