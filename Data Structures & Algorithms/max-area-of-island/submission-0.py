class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m=len(grid)
        n=len(grid[0])
        max_area=0
        directions=[(1,0),(0,1),(-1,0),(0,-1)]

        def dfs(i,j):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j]!=1:
                return 0
            area=1
            grid[i][j]=0
            for x,y in directions:
                area+=dfs(i+x,j+y)
            return area
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    max_area=max(max_area,dfs(i,j))
        return max_area