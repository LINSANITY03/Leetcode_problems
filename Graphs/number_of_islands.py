import collections

# check if the grid is 0 then return 0 as their is no islands
# initially the islands is set to 0 and visit is a set
# row and column of the grid
# iterate the grid[rows][column] if it is 1 and not visited
# then first increment the islands and dfs
# if the rows and column is in boundary and element is 0 or visited return
# then add the current position to visit
# directions in 4 direct the dfs for each direction


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        islands = 0
        visit = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if (
                r not in range(rows)
                or c not in range(cols)
                or grid[r][c] == "0"
                or (r, c) in visit
            ):
                return

            visit.add((r, c))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    islands += 1
                    dfs(r, c)
        return islands


# BFS Version From Video
class SolutionBFS:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r) in range(rows) and (c) in range(cols) and grid[r][c] == '1' and (r, c) not in visited:

                        q.append((r, c))
                        visited.add((r, c))

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1

        return islands
