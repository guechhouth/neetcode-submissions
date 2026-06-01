class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        r = len(matrix)
        c = len(matrix[0])
        zeros = []

        def zero(row,col):
            #row r and column c
            #make the entire row 0
            for i in range(c):
                if matrix[row][i] != 0:
                    matrix[row][i] = 0
            #make the entire col 0
            for j in range(r):
                if matrix[j][col] != 0:
                    matrix[j][col] = 0
            

        for row in range(r):
            for col in range(c):
                if matrix[row][col] == 0:
                    zeros.append((row,col)) #can't change the array right now
        for i,j in zeros:
            zero(i,j)
        