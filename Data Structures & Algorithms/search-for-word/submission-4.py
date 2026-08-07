class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(r,c,index):
            # check this first
            if index == len(word):
                return True
            # check bound, second to prevent index out of range
            if r < 0 or r >= rows or c < 0 or c >= cols or (r,c) in visited or board[r][c] != word[index]:
                return False
        

            visited.add((r,c))
            if word[index] == board[r][c]:
                index += 1
                found = dfs(r+1,c, index) or dfs(r -1,c, index) or dfs(r,c+1,index) or dfs(r,c-1,index)
                visited.remove((r,c)) #backtracking
                return found
    
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True
        return False       