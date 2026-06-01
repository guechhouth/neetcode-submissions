class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) -1
        while l < r:
            #go clockwise
            for i in range(r-l):
                #assign for top and bottom 
                t, b = l, r
                #save the top left
                topLeft = matrix[t][l+i]

                #move b-left to t-left
                matrix[t][l+i] = matrix[b-i][l]

                #move b-right to b-left
                matrix[b-i][l] = matrix[b][r-i]

                #move t-right to b-right
                matrix[b][r-i] =  matrix[t+i][r]

                #move t-left to t-right
                matrix[t+i][r] = topLeft
            r -= 1
            l += 1
        
        