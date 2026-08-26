class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # nested for loop
        # if curr == 1
          # check left, right, down, up
          # movet to index with 1, mark visited

        rows, cols = len(grid), len(grid[0])
        max_area = 0

        def dfs(row, col): 
            # check the top, down, left, right
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0:
                return 0 # out of bounds or 0
            
            grid[row][col] = 0 # mark visited
            return (1 + dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row, col - 1))

        for row in range(rows):
            for col in range(cols):               
                if grid[row][col] == 1:
                    area = dfs(row, col)
                    max_area = max(area, max_area) 
        
        return max_area
                        
