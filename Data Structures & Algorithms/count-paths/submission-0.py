'''
so from the tropy --> we can go up or right
x,y
x - 1, y + 1 --> these two directions

= # of ways to right + # of ways to down

stop performing this also when we reach target grid[m-1][n-1]

if we think about from the perspective of builder 
- at pos grid[0][0]: 
---> ways to reach it = 1
- then we want to go right (x+1): look at x - 1 (left) = 1
|--> (x+1) + 1
|-->  y -1: check up and right: 1 + 1 = 2
- then we want to go down (y+1): look at y - 1 = 1

#how to store such values?
2d array

'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #initalize 2d array to store each result to reuse
        res = [[1] * n] * m #mxn
        res[0][0] = 1

        for i in range(1, m):
            for j in range(1,n):
                res[i][j] = res[i-1][j] + res[i][j-1]
        return res[m-1][n-1]

        

       
       


        