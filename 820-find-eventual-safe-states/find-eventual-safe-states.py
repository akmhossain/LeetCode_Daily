class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # given adjacency list find all the safe nodes
        # safe nodes: every path leads to terminal node
            # if graph[i] = [], then safe
            # if there is a cycle, all nodes in the cycle are not safe

        # solution: dfs
        # for each node: dfs each element in the list, false if in cycle 

        unseen = 0
        visited = 1
        visiting = 2
        states = [unseen] * len(graph) # list used to keep track of node states
        def dfs(node):
            state = states[node]
            if state == visited : return True
            if state == visiting : return False # loop detected 

            states[node] = visiting

            for adj_node in graph[node]:
                if not dfs(adj_node):
                    return False
            
            states[node] = visited
            return True
        
        res = []
        for i in range(len(graph)):
            if dfs(i):
                res.append(i)
        
        return res
            

