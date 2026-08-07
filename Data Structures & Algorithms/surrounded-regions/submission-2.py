"""
have a region, within a region, none of the 0 cell should be on the edge of the board 

1. need to know if it is a region
- visited set: add 0 visited. if each cell neighbor as any is 0 and ear edge -> not valid, maybe we can check that the bound check?
- add all these to visited set so we can skip the cell 
2. know that this region is valid or not
3. replace all 0s in the region with Xs
- valid set: store one coordinate of one cell in a valid region
- explore and mark 0 to X

reverse engineer:
- traverse from the edge, add to invalid set cell that is in invalid region
- mark the other cell "x" if they are "0" and not in invalid
"""
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        invalid = set()
        
        def dfs(r,c, rows, cols):
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] == "X" or (r,c) in invalid:
                return

            if board[r][c] == "O":
                invalid.add((r,c))
                for (dr,dc) in [(0,1), (1,0), (-1,0), (0,-1)]:
                    nr = r + dr
                    nc = c + dc
                    dfs(nr, nc, rows, cols)

        # run dfs for every cell on the edge
        for r in range(rows):
            for c in [0, cols-1]:
                if board[r][c] == "O":
                    dfs(r,c, rows, cols)
        for c in range(cols):
            for r in [0, rows-1]:
                if board[r][c] == "O":
                    dfs(r,c, rows, cols)
        print(f"invalid:{invalid}")
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in invalid and board[r][c] == "O":
                    board[r][c] = "X"

            