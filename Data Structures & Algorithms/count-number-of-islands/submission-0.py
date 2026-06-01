'''
clarifying question: 
- does diagonal count?
- so I am asked to connect all the one's horizontally and vertically?
-> they will be counted as one island?

approach:
- we can do r,c and continue as long as we have 1
- at the same time, we add the coordinate we visited to the set
so that if we have visited that, then we don't need to visit it again
- when do we plus one to count? either we can't go any left, right, up, and down
without hitting the water or the coordinate that we want to visit is alr visited

- backtrack and clean up

- when we go through r,c if at (r,c) it is 0 we dont do dfs. if it is 1 then we do dfs

- how do we know that we counted the same one or not? maybe we can have another set
that store the collection of all the ones each island has

bfs approach: bfs is iterative not recursive
- visit the neighbour of each node
- add it to visited set
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        row, col = len(grid), len(grid[0])
        visited = set()
        count = 0

        def dfs(r,c): #island is to store each island
            #base case
            if (r < 0 or c < 0 or r >= row or c >= col or
                (r,c) in visited or grid[r][c] == "0"):
                return
            #if the grid is 1
            visited.add((r,c))
            #call dfs repetitively
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)

        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1" and (r,c) not in visited:
                    #do dfs
                    dfs(r,c)
                    #after a full round of dfs
                    count += 1
        return count
        