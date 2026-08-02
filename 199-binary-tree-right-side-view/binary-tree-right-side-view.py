# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # BFS solution, right-most element before moving onto next level
        # OR post-order DFS

        if not root:
            return []

        dq = deque([root]) # contains reference to node
        bfs = [] # contains node values
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

            bfs.append(lvl)
        
        # copied from leetcode 102 lvl order traversal: output is list of level lists
        # e.g. [[1], [2,3]]
            
        return [lvl[-1] for lvl in bfs]
