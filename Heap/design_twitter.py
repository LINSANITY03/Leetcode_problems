from collections import defaultdict
import heapq


class Twitter:
    # initialize count, defaultdict for tweetMap and followMap
    def __init__(self):
        self.count = 0
        # userId -> list of [count, tweetIds]
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)  # userId -> set of followeeId

    # for each userId add count twitter post and tweetid
    # then decrement the value since we use minHeap
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    # add userid in followMap on itself
    # every people this id follows get pointer and tweet count then add to minHeap
    # add the recent 10 tweetid if a tweeter has more tweets get recent by minheap ocunt
    def getNewsFeed(self, userId: int) -> list[int]:
        res = []
        minHeap = []
        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(
                    minHeap, [count, tweetId, followeeId, index - 1])

        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(
                    minHeap, [count, tweetId, followeeId, index - 1])
        return res

    # adding followers in hashmap
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    # if value in hashmap then remove the id
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
