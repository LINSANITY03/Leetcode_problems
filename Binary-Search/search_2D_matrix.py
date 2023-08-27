# 0(log(m*n))

# initialize rows and cols of the matrix
# we need find in which row the number reside
# initialize top and bot as 0 and rows-1 length
# to know if it reside on a row check the lowest and biggest value on l and r
# if target is greater than right most then target is in other part
# if less than leftmost then leftmost than this row
# else it is in current row
# use binary search on that row

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1
        while top <= bot:
            row = top + ((bot - top) // 2)
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        if not (top <= bot):
            return False
        row = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = l + ((r - l) // 2)
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3

print(Solution().searchMatrix(matrix, target))
