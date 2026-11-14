class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(r, c, i):
            # exit
            if i == len(word): # found the word
                return True

            # check valid boundaries
            if r < 0 or r > len(board)-1 or c < 0 or c > len(board[0])-1 or board[r][c] != word[i]:
                return False

            temp = board[r][c]

            board[r][c] = "#"

            # find neighbors
            # U, D, R, L
            found = (
                dfs(r-1, c, i+1) or 
                dfs(r+1, c, i+1) or 
                dfs(r, c+1, i+1) or 
                dfs(r, c-1, i+1)
            )

            board[r][c] = temp

            return found
            

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0): 
                        return True

        return False