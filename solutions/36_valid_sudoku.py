from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rowDict = defaultdict(set)
        colDict = defaultdict(set)
        squareDict = defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if (
                    board[row][col] in rowDict[row] or
                    board[row][col] in colDict[col] or
                    board[row][col] in squareDict[(row // 3, col // 3)]
                    ):
                    return False
                rowDict[row].add(board[row][col])
                colDict[col].add(board[row][col])
                squareDict[(row // 3, col // 3)].add(board[row][col])
        return True
