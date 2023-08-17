from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check row
        for i in range(9):
            row = []
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] not in row:
                        row.append(board[i][j])
                    else:
                        return False
        # Check column
        for i in range(9):
            column = []
            for j in range(9):
                if board[j][i] != ".":
                    if board[j][i] not in column:
                        column.append(board[j][i])
                    else:
                        return False
        # Check 3x3 boxes
        box = 1
        row = 0
        col = 0
        while box <= 9:
            if box % 3 == 1:
                row = 0

            if box <= 3:
                col = 0
            elif box <= 6:
                col = 3
            else:
                col = 6

            in_box = []

            for i in range(row, row + 3, 1):
                for j in range(col, col + 3, 1):
                    if board[i][j] != ".":
                        if board[i][j] not in in_box:
                            in_box.append(board[i][j])
                        else:
                            return False
            row += 3
            box += 1

        return True
