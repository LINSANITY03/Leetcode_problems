# OAKNORTH BANK - JUNIOR PYTHON ENGINEER - INTERVIEW QUESTION

# Time complexity O(m * n) --> m=rows, n=cols

# First initialize default dictionary of type set for column, row and square
# for every row and column, we add _row_index and _cols_index as key and value as set
# to find square in board, we need to divide the range with 3 as absolute value
# such as for row 0 -> abs(0 or 1 or 2 //3) is 0
# (3 or 4 or 5) // 3 is 1
# (6 or 7 or 8) // 3 is 2
# such that we cut 9*9 into [[0,0], [0,1], [0,2], [1,0], [1,1], [1,2], [2,0], [2,1], [2,2]]
# then we can check validity

import collections


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)  # key = (r /3, c /3)

        for r in range(9):
            for c in range(9):

                if board[r][c] < 1 and board[r][c] > 9:
                    return False

                if (
                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]
                ):
                    return False

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        print('cols', cols, end='\t')
        print('rows', rows)
        print('squares', squares)
        print(3 // 2)
        return True


passing_example = [
    [5, 1, 7, 6, 9, 8, 2, 3, 4],
    [2, 8, 9, 1, 3, 4, 7, 5, 6],
    [3, 4, 6, 2, 7, 5, 8, 9, 1],
    [6, 7, 2, 8, 4, 9, 3, 1, 5],
    [1, 3, 8, 5, 2, 6, 9, 4, 7],
    [9, 5, 4, 7, 1, 3, 6, 8, 2],
    [4, 9, 5, 3, 6, 2, 1, 7, 8],
    [7, 2, 3, 4, 8, 1, 5, 6, 9],
    [8, 6, 1, 9, 5, 7, 4, 2, 3]]

# passing_example = [
#     [5, 1, 7, 6, 9, 8, 0, 3, 4],
#     [0, 8, 9, 1, 3, 4, 7, 5, 6],
#     [3, 4, 6, 0, 7, 5, 8, 9, 1],
#     [6, 7, 0, 8, 4, 9, 3, 1, 5],
#     [1, 3, 8, 5, 0, 6, 9, 4, 7],
#     [9, 5, 4, 7, 1, 3, 6, 8, 0],
#     [4, 9, 5, 3, 6, 0, 1, 7, 8],
#     [7, 0, 3, 4, 8, 1, 5, 6, 9],
#     [8, 6, 1, 9, 5, 7, 4, 0, 3]]

print(Solution().isValidSudoku(passing_example))
