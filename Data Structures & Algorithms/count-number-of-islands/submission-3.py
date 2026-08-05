"""
using dfs for this:
- every time, we reach an island we do dfs on each nei if it is an island and not already visited
- count is a global variable that will keep track of the number of island

another approach is to mark each cell 0 after viisiting if it is 1
this way we wont need a visited set
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # init 
        visited = set()
        count = 0
        rows, cols = len(grid), len(grid[0])

        # dfs
        def dfs(r,c, rows, cols):
            # check for boundary
            if r < 0 or r >= rows or c < 0 or c >= cols or (r,c) in visited:
                return
            
            # add to visit
            if grid[r][c] == "1": # number here is string
                visited.add((r,c)) 
                # call on 4 direction
                for (dr,dc) in ([0,1], [0,-1], [1,0], [-1,0]):
                    dfs(r+dr, c+dc, rows, cols)
          

        # go through each position on the grid, skipped one we already visited
        for r in range(rows):
            for c in range(cols):
                # only check when the cell is not yet visited and is an land
                if (r,c) not in visited and grid[r][c] != "0":
                    # dfs
                    dfs(r,c, rows, cols)
                    count += 1 # one connected island found
                
        return count



        

        