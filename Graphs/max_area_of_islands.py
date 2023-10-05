# get the rows and column length
# create set for visited position
# initial area is 0
# for each position we need to do dfs but this time we need to check area
# for each position check if its inside boundary and element is 0 and is not visited then return 0
# add current position to visit
# each iteration has 1 added to area then as in all dfs we need to add dfs of 4 direction
class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            if (
                r < 0
                or r == ROWS
                or c < 0
                or c == COLS
                or grid[r][c] == 0
                or (r, c) in visit
            ):
                return 0
            visit.add((r, c))
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, dfs(r, c))
        return area
