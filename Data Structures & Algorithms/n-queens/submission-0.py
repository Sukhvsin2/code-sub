class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        res = []

        board = [['.']*n for i in range(n)]

        col = set()
        posD = set()
        negD = set()

        def backtrack(r):

            # exit
            if r == n: # last row
                res.append(["".join(row) for row in board])
                return

            for c in range(n):
                if c in col or (r-c) in posD or (r+c) in negD:
                    continue

                col.add(c)
                posD.add(r-c)
                negD.add(r+c)
                board[r][c] = "Q"
                backtrack(r+1) # check in next row
                board[r][c] = "."
                col.remove(c)
                posD.remove(r-c)
                negD.remove(r+c)
                
        backtrack(0)
        return res

