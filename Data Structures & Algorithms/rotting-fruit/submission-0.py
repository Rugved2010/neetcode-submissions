class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows=len(grid)
        cols=len(grid[0])
        fresh=0
        q=deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    fresh+=1
                elif grid[i][j]==2:
                    q.append((i,j))
        
        if fresh==0:
            return 0

        minutes=0
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        while q and fresh>0:
            for _ in range(len(q)):
                r,c=q.popleft()
                for nr,nc in directions:
                    dr=nr+r
                    dc=nc+c
                    if dr<0 or dr>=rows or dc<0 or dc>=cols or grid[dr][dc]!=1:
                        continue
                    grid[dr][dc]=2
                    fresh-=1
                    q.append((dr,dc))
            minutes+=1
        return minutes if fresh==0 else -1
            
        