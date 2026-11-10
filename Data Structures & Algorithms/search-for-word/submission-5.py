class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        visited = set()

        def dfs(row, col, i):

            # found it?
            if i == len(word): 
                return True

            # print(f"entered in dfs where r,c,i : {row}, {col}, {i}")
            # print(f"visited : {visited}")

            # check boundaries
            # print(f"check : {row} {col} and word i : {i}")
            if row < 0 or col < 0 or row > len(board)-1 or col > len(board[0])-1  or (row,col) in visited or board[row][col] != word[i]:
                # print("returning since wrong match")
                return False # stale path

            # check all 4 paths - U, D, R, L
            visited.add((row, col))
            found = (
                dfs(row-1, col, i+1) or 
                dfs(row+1, col, i+1) or
                dfs(row, col+1, i+1) or
                dfs(row, col-1, i+1)
            )

            visited.remove((row,col))
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