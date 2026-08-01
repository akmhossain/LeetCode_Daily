# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # pre-order: root-l-r, inorder = l-root-right
        # the first element in pre-order is root
        # find root in in-order: left is left subtree, right is right subtree

        # recursion question to ask: where can I reuse the code above, when winding up or down(pruning down)
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])

        # for inorder return the correct half, for preorder left skip 1st value (root) and return up until mid
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root
