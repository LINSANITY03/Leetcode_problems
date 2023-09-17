import heapq

# we are using heapq to return k largest
# it is a data stream such that after a initialize the list there might be more data added
# initialize a heapify by using heapq.heapify
# since we need only k elements
# anything more than k can be discarded
# while adding check if it more than k else return minheapq


class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        # minHeap w/ K largest integers
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]


Kthobj = KthLargest(3, [4, 5, 8, 2])
print(Kthobj.add(3))  # return 4
print(Kthobj.add(5))  # return 5
print(Kthobj.add(10))  # return 5
print(Kthobj.add(9))  # return 8
print(Kthobj.add(4))
