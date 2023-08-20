# array approach

# initalize result
# starting price as the lowest price
# for every value: check if the price is lower than current price
# if yes: lowest = current price then calculate the profit = max(res, price - lowest)

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        res = 0

        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            res = max(res, price - lowest)
        return res

# two - pointer approach
# intialize the pointer to first and second index
# set max profit as 0
# while right pointer is less than len(prices):
#   if prices of left pointer is less than right calucate the profit with currentmax
# else set the left pointer to right as we got new high
# increase the right pointer by 1 on each iteration


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r < len(prices):

            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r

            r += 1
        return maxP
