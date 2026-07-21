class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # given adjacency list find all the safe nodes
        # safe nodes: every path leads to terminal node
            # if graph[i] = [], then safe
            # if there is a cycle, all nodes in the cycle are not safe

        # solution: dfs
        # for each node: dfs each element in the list, false if in cycle 

        n = len(graph)
        state = [0] * n

        def dfs(node): # detect cycles
            if state[node] != 0: # if visited or visiting
                return state[node] == 2 # if visiting(1) then false: cycle

            state[node] = 1 # mark node visiting

            for nei in graph[node]: # executes on unseen nodes
                if not dfs(nei):
                    return False

            # mark visited and return true (no cycle detected)
            state[node] = 2
            return True
        
        res = []
        for i in range(len(graph)):
            if dfs(i):
                res.append(i)
        
        return res
            

