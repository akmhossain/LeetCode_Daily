from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # ways to represent a directed graph: adjacency matrix or dictionary
        # given a constructed graph, return false if cycle detected
        # dfs through the nodes, with three states
        # if visited then no problem, if visiting node and comes back to a visting node (False)

        # build adjacency matrix: key is the node, value is the nodes it points to
        course_graph = defaultdict(list)
        for a,b in prerequisites: 
            course_graph[b].append(a) 

        # dfs to detect cycles
        # unseen - 0, visiting - 1, visited - 2 
        state = [0] * numCourses
        def dfs(node): 
            if state[node] != 0: 
                return state[node] == 2

            state[node] = 1

            for nei in course_graph[node]:
                if not dfs(nei):
                    return False

            state[node] = 2
            return True
        
        # actual loop to trigger dfs
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        # DFS did not find any cycles in graph
        return True
