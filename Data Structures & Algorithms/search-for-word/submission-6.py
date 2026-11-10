class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        # visited = set()

        def dfs(row, col, i):

            # found it?
            if i == len(word): 
                return True

            if row < 0 or col < 0 or row > len(board)-1 or col > len(board[0])-1 or board[row][col] != word[i]:
                return False # stale path

            # check all 4 paths - U, D, R, L
            val = board[row][col]
            board[row][col] = "#"
            found = (
                dfs(row-1, col, i+1) or 
                dfs(row+1, col, i+1) or
                dfs(row, col+1, i+1) or
                dfs(row, col-1, i+1)
            )

            board[row][col] = val
            return found


        # first need to find first letter ref on the grid
        for r in range(len(board)):
            for c in range(len(board[0])):
                if word[0] == board[r][c]:
                    # do DFS on every ref's path on the grid
                    if dfs(r, c, 0): # row, col, word[i]
                        return True
        # default
        return False 