class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        square = collections.defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                
                if (board[i][j] in rows[i] or 
                    board[i][j] in cols[j] or 
                    board[i][j] in square[(i//3,j//3)]):
                    return False

                rows[i].add(board[i][j])
                cols[j].add(board[i][j])

                square[i//3, j//3].add(board[i][j])

                print("rows: ", rows)
                print("cols: ", cols)
                print("square: ", square)

        return True