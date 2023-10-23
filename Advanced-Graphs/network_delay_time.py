import heapq
import collections

# bfs, heapq, hashmap
# create a hashmap with source as key and (destination, cost) as value
# since we are given a point in start we can create 0 cost and point itself as first point of contact
# then we need to pop the first value then if the point is not in visit add to visit and for its edges
# add the cost with initial at point new


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))
        # defaultdict(<class 'list'>, {2: [(1, 1), (3, 1)], 3: [(4, 1)]})
        minHeap = [(0, k)]
        visit = set()
        t = 0
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            t = w1

            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1 + w2, n2))
        return t if len(visit) == n else -1


times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
n = 4
k = 2
print(Solution().networkDelayTime(times, n, k))
