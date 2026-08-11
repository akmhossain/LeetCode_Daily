# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque 
# left to right, right to left
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS loop while queue
        # bool to keep track of direction set off each lvl
        if not root:
            return []
        dq = deque([root])
        res = []
        leftToRight = False

        while dq:
            curr = []
            for i in range(len(dq)):
                node = dq.popleft()
                curr.append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            if leftToRight:
                curr.reverse()
                res.append(curr)
                leftToRight = False
            else:
                res.append(curr)
                leftToRight = True

        return res