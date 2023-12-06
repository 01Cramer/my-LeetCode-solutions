class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        first_row = 0
        last_row = rows - 1

        while first_row <= last_row:
            middle_row = (first_row + last_row) // 2
            if matrix[middle_row][0] == target:
                return True

            elif matrix[middle_row][0] < target:  # Can be in the same row or in one of the next rows
                first_col = 0
                last_col = cols - 1

                while first_col <= last_col:
                    middle_col = (first_col + last_col) // 2
                    if matrix[middle_row][middle_col] == target:
                        return True
                    elif matrix[middle_row][middle_col] < target:
                        first_col = middle_col + 1
                    else:
                        last_col = middle_col - 1

                first_row = middle_row + 1  # not found in the same row

            else:
                last_row = middle_row - 1

        return False