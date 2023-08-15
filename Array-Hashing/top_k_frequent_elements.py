# to find the optimal solution of O(n)
# we need to count the frequency using hashmap
# then we can create a list with index as frequency and value as the number
# [1, 1, 1] ----> [[], [], 1] --> 1 is in 3rd position meaning it is repeated 3 times
# then we append the list from last to first and check the length with our target
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        print(freq)

        for n in nums:
            count[n] = 1 + count.get(n, 0)
            print(count)

        for n, c in count.items():
            freq[c].append(n)

        print(freq)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                print('res & k', res, k)
                if len(res) == k:
                    return res

        # O(n)


nums = [1, 1, 1, 2, 2, 3]
k = 2

print(Solution().topKFrequent(nums, k))
