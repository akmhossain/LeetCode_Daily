class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])

        def dfs(i,j): # dfs will recursively check for neighboring 1s and flip into 0
            if i < 0 or i >= row or j < 0 or j >= col or grid[i][j]=='0':
                return # i or j is out of bounds
            else:
                grid[i][j] = '0'
                dfs(i+1, j) # bottom
                dfs(i-1, j) # top
                dfs(i, j+1) # right 
                dfs(i, j-1) # left

        count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    dfs(i,j)
                    count += 1
        
        return count
