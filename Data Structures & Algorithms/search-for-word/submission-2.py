'''
the board  can be any shape? or square or rectangle
can the word be in the board more than once?

approach
#base case to continue:
return when next char in word is not = next visit
#base case when true:
return true when last char in word = next character
#base case when false:
return false when last char in word != next character 

when an equal char is seen -> we potentially need to check the next row. how? second function with
column c as parameter: total column = len(board)

how to make sure if we visit same character on board? use set and add to set if alr visited

'''

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''
        #get column and row
        row, col = len(board), len(board[0])
        #avoid repetition
        path = set()

        def dfs(r,c,i):
            if i == len(word):
                return True
        
            if r<0 or c <0 or r >= row or c >= col or word[i] != board[r][c] or (r,c) in path:
                return False
            path.add((r,c))
            res = (dfs(r+1, c, i+1) or dfs(r-1, c, i+1) or dfs(r, c+1, i+1) or dfs(r, c-1, i+1))
            path.remove((r,c))
            return res
        for r in range(row):
            for c in range(col):
                if dfs(r,c,0): return True
        return False
        '''
        row, col = len(board), len(board[0])
        path = set()

        def dfs(r,c,index):
            if len(word) == index:
                return True

            if r < 0 or c < 0 or r >= row or c >= col or board[r][c] != word[index] or (r,c) in path:
                return False
            
            path.add((r,c))
            if board[r][c] == word[index]:
                index +=1
            found = dfs(r+1,c,index) or dfs(r-1,c,index) or dfs(r,c+1,index) or dfs(r,c-1,index)
            path.remove((r,c))
            return found
        
        for r in range(row):
            for c in range(col):
                if dfs(r,c,0):
                    return True
        return False
            




        