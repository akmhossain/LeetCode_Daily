from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # solve using topological sort
        adj = defaultdict(list)
        in_d = {v:0 for v in range(numCourses)} # indegree tracker

        for u,v in prerequisites:
            adj[u].append(v)
            in_d[v] += 1
        
        # start q with nodes without anything pointing to it
        q = deque([v for v in range(numCourses) if in_d[v] == 0])
        order = []
    
        while q:
            u = q.popleft()
            order.append(u)
            
            for v in adj[u]:
                in_d[v] -= 1
                if in_d[v] == 0:
                    q.append(v)
                    
        # If order doesn't include all vertices, there is a cycle
        if len(order) != numCourses:
            return False
            
        return True

    # when theres a loop there will remain atleast one vertex whose indegree was more than one so it never got appended to order