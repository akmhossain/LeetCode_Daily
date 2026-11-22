"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # dfs and then hashmap of new:old nodes
        if not node:
            return None

        h = {} # keys are old reference, values are new 

        def dfs(curr):
            if curr in h:
                return
            h[curr] = Node(val=curr.val)
            for nei in curr.neighbors:
                dfs(nei)
        
        dfs(node)

        # build new graph, use old reference links but get the new nodes from h
        for old, new in h.items():
            for nei in old.neighbors:
                new.neighbors.append(h[nei])
        
        return h[node]

        