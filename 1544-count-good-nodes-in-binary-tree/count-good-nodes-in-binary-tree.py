# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # if not root then return 0, else res = 1
        # dfs left/right
        # maintain a max value, if curr node is greater= then res += 1
        if not root:
            return 0
        
        def dfs(node, max_val): # node, max_val are local, changes every call
            res = 0
            # base case
            if not node:
                # return unwinds one call from stack
                return 0 

            if node.val >= max_val:
                res += 1
                max_val = node.val

            l = dfs(node.left, max_val) 
            r = dfs(node.right, max_val) 

            return res + l + r

        return dfs(root, root.val)
            