# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        # implementation of BFS with deque
        # queue up pointers to left and right of curr, process each following element in the queue the same way
        if not root:
            return []

        dq = deque([root]) # contains reference to node
        res = [] # contains node values
        while dq:
            lvl = []
            n = len(dq)
            for i in range(n):
                curr = dq.popleft()
                lvl.append(curr.val)

                if curr.left:
                    dq.append(curr.left)
                if curr.right:
                    dq.append(curr.right) 

            res.append(lvl)
            
        
        return res
