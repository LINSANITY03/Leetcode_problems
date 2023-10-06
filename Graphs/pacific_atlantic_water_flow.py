# initiate the rows and columns
# then we need to create a visited from pacific and atlantic part. so we create set()
# we know the first column touches pacific and last column touches atlantic ocean
# so for each row we use dfs on first column element and last column element
# but we need to use pacific and atlantic for first and last column visited set
# instead of checking every element we can check before hand if the position touches any other region.
# for each position check if it is not visited and inside the boundary and if current element is smaller
# than the previous then just return
# else use same dfs for all four direction
# use same for height we did the length part before(from picture length and breadth)
# then we need to create a result list to return the position
# if the position in pac and atlantic we know it touches both region so append to res

class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            if (
                (r, c) in visit
                or r < 0
                or c < 0
                or r == ROWS
                or c == COLS
                or heights[r][c] < prevHeight
            ):
                return
            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res


heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [
    2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
print(Solution().pacificAtlantic(heights))
