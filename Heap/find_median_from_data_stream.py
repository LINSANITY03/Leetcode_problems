import heapq

# first we need to initialize two lists from small and large data for adding object in 0(1).
# before adding any number check if it belongs to large list else add to small.
# but before adding in small put negative since we are using minheap on it.
# check the length of two lists if the difference is more than one we need to stabilize it.
# check the smallest in small and first on large and compare then pop and add to large else reverse.
# ig the length of any of two lists is not same just return the smallest out of the biggest one.
# if it is equal then we need to find average of sum of smallest from both lists


class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        # two heaps, large, small, minheap, maxheap
        # heaps should be equal size
        self.small, self.large = [], []  # maxHeap, minHeap (python default)

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1 * num)

        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0]) / 2.0
