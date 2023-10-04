# we need to create sets for column, position and negative diagonal
# create empty list to return output
# initialize the n * n list with "." string
# initialize the backtrack with 0 as row, we need to check up to n since it is a n*n matrix

# for each iteration, we cannot put more than 1 queen in a column, r+c should not be posiive diagonal
# and r-c should not be in a negative diagonal
# this is because all the diagonal gives same value such that we can identify a unique diagonal
# if the current column of first row is in column set then continue without doing anything
# add the current column to col set
# then add the r+c, r-c in positive and negative diagonal respectively
# then replace the "." string to "Q" as a queen for this iteration
# then backtrack increasing the row+1
# remove the current column as a classic backtrack approach
# remove the positive and negative diagonal value
# board to "." backtracking from "Q"
class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        col = set()
        posDiag = set()  # (r + c)
        negDiag = set()  # (r - c)

        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return res


print(Solution().solveNQueens(4))
