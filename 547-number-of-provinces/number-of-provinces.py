class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        n = len(isConnected)
        provinces = 0

        # dfs will visit all of i's adjacent nodes and add to set
        def dfs(i):
            visited.add(i) 
            for j in range(n):
                if isConnected[i][j] and j not in visited: # if j not in set
                    dfs(j) # return j (neighbor) and next call will add to set

        # loop to trigger dfs if node not in set
        for i in range(n):
            if i not in visited: 
                provinces += 1
                dfs(i)

        return provinces 
