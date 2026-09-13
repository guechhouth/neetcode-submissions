"""
input: 
- grid: grid[i] is 0 or 1
--> 0: water
--> 1: land

area = number of cells within the island

"""

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        self.max_area = 0

        def dfs(r,c):
            if r < 0 or c < 0 or r >= rows or c >= cols or (r,c) in visited:
                return
            
            if grid[r][c] == 1:
                visited.add((r,c))
                self.area += 1
                #print(f"area: {self.area}, max_area: {self.max_area}")
                for (dr,dc) in ([0,1], [1,0], [-1,0], [0,-1]):
                    # print(f"grid[{r}][{c}]: {grid[r][c]}")
                    # print(f"{i[0]}, {i[1]}")
                    dfs(r+dr, c+dc)
            
        for r in range(rows):
            for c in range(cols):
                self.area = 0
                if grid[r][c] == 1 and (r,c) not in visited:
                    # print(f"r,c: [{r}][{c}] = {grid[r][c]}")
                    dfs(r,c)
                    self.max_area = max(self.max_area, self.area)
        return self.max_area

        