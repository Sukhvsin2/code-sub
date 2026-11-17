class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        cols = set()
        negD = set()
        posD = set()
        board = [["."]*n for i in range(n)]

        def backtrack(r):
            
            if r == n: # at last row
                res.append(["".join(row) for row in board])
                return 

            for c in range(n):
                if c in cols or (r-c) in posD or (r+c) in negD:
                    continue # skip since we can't put Queen there.

                board[r][c] = "Q"
                cols.add(c)
                posD.add(r-c)
                negD.add(r+c)

                backtrack(r+1)
                board[r][c] = "."
                cols.remove(c)
                posD.remove(r-c)
                negD.remove(r+c)


        backtrack(0) # start processing first row
        return res