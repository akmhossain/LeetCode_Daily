# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # record the depth of left and right subtrees
        # pre order is n^2(checks at each node again), post order is n
        if not root:
            return True
        
        self.balanced = True
        
        def balance(node):
            if not node:
                return 0
            left, right = balance(node.left), balance(node.right)
            if abs(right - left) > 1:
                self.balanced = False
            return max(left, right) + 1

        balance(root)
        return self.balanced             



        
        

            
            


