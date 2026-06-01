'''
so the idea is to visit different height and form path as long as we can
- maybe add the coordinate path in a hashmap to keep track
- bfs to check the neighbor -> queue and add all neighbor and popleft

- how to stop continuing with a specific path? 
- how to know if we start from which ocean and when we we reached?
--> store r,c for pacific side
pacific: heights[0][0] - heights[0][]
        heights[0][0] - heights[len(heights)-1][0]
atlantic: heights[len(heights)-1][0] - heights[len(heights)-1][len(heights[0] - 1)]
        heights[len(heights)-1][0] - heights[len(heights)-1][len(heights[0] - 1)]

--> store r,c for atlantic


'''

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row, col = len(heights), len(heights[0])
        pac, alt = set(), set()

        #for each iteration, we should start at the opposite side
        #go as deep as possible using dfs
        #backtracking
        #visited set: if both end visit the same element, then we found ther route

        def dfs(r,c, visit, prevHeight):
            #base case
            if (r,c) in visit or r < 0 or c < 0 or r >= row or c >= col or heights[r][c] < prevHeight:
                return 
            visit.add((r,c))
            dfs(r+1,c,visit, heights[r][c])
            dfs(r-1,c,visit, heights[r][c])
            dfs(r,c+1,visit, heights[r][c])
            dfs(r,c-1,visit, heights[r][c])

        #go throw the  row
        for c in range(col):
            #for pacific row
            dfs(0,c,pac,heights[0][c])
            #for atlantic row
            dfs(row-1,c,alt,heights[row-1][c])
        #go throw the col
        for r in range(row):
            #for pacific col
            dfs(r,0,pac,heights[r][0])
            #for atlantic col
            dfs(r,col-1,alt,heights[r][col-1])
        
        res = []
        for r in range(row):
            for c in range(col):
                if (r,c) in pac and (r,c) in alt:
                    res.append([r,c])
        return res
        

            

        