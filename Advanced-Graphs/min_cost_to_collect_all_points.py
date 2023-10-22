# hashmap + minheap
# first create a empty heap to append distance between any two points
# we will have a collection of list of [cost, index] from each to every nodes
# prim's algorithm
# create a set to track visited nodes
# minheap with 0 as a cost to connect to itself (cost, index)
# while we are not visiting every nodes
# get the min cost to reach a node then add the index to visit and increase the result
# for the selected index, traverse through other index connected and if no visited add to minheap
# cost and index
import heapq
import pprint


class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        N = len(points)
        adj = {i: [] for i in range(N)}  # i : list of [cost, node]
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        pprint.pprint(adj)
        '''
        {0: [[4, 1], [13, 2], [7, 3], [7, 4]],
        1: [[4, 0], [9, 2], [3, 3], [7, 4]],
        2: [[13, 0], [9, 1], [10, 3], [14, 4]],
        3: [[7, 0], [3, 1], [10, 2], [4, 4]],
        4: [[7, 0], [7, 1], [14, 2], [4, 3]]}
        '''
        # Prim's
        res = 0
        visit = set()
        minH = [[0, 0]]  # [cost, point]
        while len(visit) < N:
            cost, i = heapq.heappop(minH)
            if i in visit:
                continue
            res += cost
            visit.add(i)
            for neiCost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minH, [neiCost, nei])
        return res


points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
print(Solution().minCostConnectPoints(points))
