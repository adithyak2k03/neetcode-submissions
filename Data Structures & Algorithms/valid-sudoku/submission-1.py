class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rowscheck = defaultdict(set)
        colscheck = defaultdict(set)
        squarescheck = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c]==".":
                    continue
                if (board[r][c] in rowscheck[r]) or (board[r][c] in colscheck[c]) or (board[r][c] in squarescheck[(r//3,c//3)]):
                    return False

                rowscheck[r].add(board[r][c])
                colscheck[c].add(board[r][c])
                squarescheck[(r//3,c//3)].add(board[r][c])

        return True

