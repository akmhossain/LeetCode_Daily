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

        # states and dfs
        # unseen, visiting, visited 
        unseen = 0
        visited = 1
        visiting = 2
        states = [unseen] * numCourses # list used to keep track of course states
        def dfs(node):
            state = states[node]
            if state == visited : return True
            if state == visiting : return False # loop detected 

            states[node] = visiting

            for adj_node in course_graph[node]:
                if not dfs(adj_node):
                    return False
            
            states[node] = visited
            return True
        
        # actual loop to trigger dfs
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        # DFS did not find any cycles in graph
        return True
