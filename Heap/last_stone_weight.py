import heapq

# here we are working with the negative value of the list
# such that we can make highest value to lowest and heapq to pop the element
# first convert the list to negative and heapify it
# if the length is none add 0 onto the heap
# else pop the biggest(smallest as we put negative) and second biggest
# perform subtraaction and add to queue
# continue until there is one item left then return the item


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)
            print(stones)
        stones.append(0)
        return abs(stones[0])


stones = [2, 7, 4, 1, 8, 1]
print(Solution().lastStoneWeight(stones))
