from collections import defaultdict, Counter

# so we need to check if the word is in the board
# firstly get the rows and column of the board
# then set the path variable by which we can know which path we have seen, it must be set no duplicates
# for every item in the board we check if the first element in the word matches
# optimizing the process, reverse the word if word[0]>word[-1]
# such that we have less head when we start
# count the total number in the board, to get proper value and key
# check the boundary of the rows, column
# count of word doesn't match the count of same element in the board
# path is already visited
# return false
# else add the (r, c) to the path
# then check 4 directions for the next items by doing i+1
# then remove the path and return the results after travelling 4 directions


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (
                min(r, c) < 0
                or r >= ROWS
                or c >= COLS
                or word[i] != board[r][c]
                or (r, c) in path
            ):
                return False
            path.add((r, c))
            res = (
                dfs(r + 1, c, i + 1)
                or dfs(r - 1, c, i + 1)
                or dfs(r, c + 1, i + 1)
                or dfs(r, c - 1, i + 1)
            )
            path.remove((r, c))
            return res

        # To prevent TLE,reverse the word if frequency of the first letter is more than the last letter's
        count = defaultdict(int, sum(map(Counter, board), Counter()))
        print(count)
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False

    # O(n * m * 4^n)


board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"
print(Solution().exist(board, word))
