"""
fresh fruit (1) next to rotton fruit (2) --> get rotten
- we mark fresh fruits rotten: 1 -> 2

how do we know all the fruits are rotten now ?
- need to do another traversal to check that everything is 2 or 0
--> not sure if this is a good idea

- if a cell is fresh fruits bit is surrounded by empty cell -> impossible. how do we detect this?

- keep count as we traverse and check against the total size of the grid --> keep te fresh count and then decrement by one every time we rot it

Minutes count by layer -> bfs is perfect for this
"""
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh = 0

        q = deque()
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c,0))
                elif grid[r][c] == 1:
                    fresh += 1
        minutes = 0        
        while q:
            r,c, m = q.popleft()
            minutes = max(m, minutes)

            # spoiling neighbours
            for (dr,dc) in [(0,1), (1,0), (-1,0), (0,-1)]:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue

                if grid[nr][nc] == 2 or grid[nr][nc] == 0:
                    continue
                
                q.append((nr,nc, m+1))
                # mark neighbour rotten
                grid[nr][nc] = 2
                fresh -=1
        
        if fresh == 0:
            return minutes
        else:
            return -1
        