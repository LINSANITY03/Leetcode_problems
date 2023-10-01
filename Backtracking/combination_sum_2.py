# we need to sort the input list such that we dont reuse the elements
# we need to send empty subset, initial 0 index, target as parameter
# if the target is 0 then copy the subset and append to results
# if target is less than 0 reject the process and return
# use loop from current initial 0 index to range of list
# if current value is equal to previuos the skip
# append the value to subset
# backtrack with subset, +1 pos and target-current value to next iteration
# then pop the value and set the current to prev for next iteration
class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()

        res = []

        def backtrack(cur, pos, target):
            if target == 0:
                res.append(cur.copy())
                return
            if target <= 0:
                return

            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue
                cur.append(candidates[i])
                backtrack(cur, i + 1, target - candidates[i])
                cur.pop()
                prev = candidates[i]

        backtrack([], 0, target)
        return res


candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
print(Solution().combinationSum2(candidates, target))
