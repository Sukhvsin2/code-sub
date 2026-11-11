class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS, COLS = len(board), len(board[0])

        # dfs to check every path
        def dfs(row, col, i):
            
            # exit
            if i == len(word):
                return True # found the word

            # check boundaries
            # check if already Visited
            if row < 0 or col < 0 or row > ROWS-1 or col > COLS-1 or board[row][col] != word[i]:
                return False

            temp = board[row][col]
            # marked visited
            board[row][col] = "#" 

            # check neighbours
            # U, D, R, L
            found = (
                dfs(row-1, col, i+1) or
                dfs(row+1, col, i+1) or
                dfs(row, col+1, i+1) or
                dfs(row, col-1, i+1)
            )
            
            # mark unvisited after checking neighbors
            board[row][col] = temp

            return found


        # find first occurance
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]: # found occ then we can find neighbors
                    if dfs(r, c, 0): return True # if we have full word return True
        

        return False # default