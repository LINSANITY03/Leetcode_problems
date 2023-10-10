import collections


class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """

# create a set for tracking visiting sets
# create a queue for bfs
# if the position is gate add to the queue and visited set
# since the distance from walls to itself is 0
# we initialize the dist as 0
# do this for 4 directional
    def walls_and_gates(self, rooms: list[list[int]]):
        ROWS, COLS = len(rooms), len(rooms[0])
        visit = set()
        q = collections.deque()

        def addRooms(r, c):
            if (
                min(r, c) < 0
                or r == ROWS
                or c == COLS
                or (r, c) in visit
                or rooms[r][c] == -1
            ):
                return
            visit.add((r, c))
            q.append([r, c])

        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                rooms[r][c] = dist
                addRooms(r + 1, c)
                addRooms(r - 1, c)
                addRooms(r, c + 1)
                addRooms(r, c - 1)
            dist += 1
