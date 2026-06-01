class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])

        visited = set()
        def dfs(r,c, index):
            if len(word) == index:
                return True
            if r >= row or c >= col or c < 0 or r < 0 or (r,c) in visited or board[r][c] != word[index]:
                return False
        
            visited.add((r,c))
            if board[r][c] == word[index]:
                index += 1
            found = dfs(r+1, c, index) or dfs(r-1, c, index) or dfs(r,c+1, index) or dfs(r,c-1, index)
            visited.remove((r,c))
            return found

        for r in range(row):
            for c in range(col):
                if dfs(r,c,0):
                    return True
        return False

        