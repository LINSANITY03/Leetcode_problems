# we are using temp table to edit the price value
# initially the price are set as inifinity for each number
# since the src and destination are given
# the price for src to src is 0
# since we are given k stops we are looping to k+1 times
# then we partially copy the prices list
# then we will go through the flights list and add the current p to edit the price
# we continue until the loop closes
# if price of destination is still infinity that means it is unchanged
# which means we cannot reach the destination from src in k steps then return -1
class Solution:
    def findCheapestPrice(
            self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:

        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):
            tmpPrices = prices.copy()

            for s, d, p in flights:
                if prices[s] == float("inf"):
                    continue
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            prices = tmpPrices
        return -1 if prices[dst] == float("inf") else prices[dst]
