# initiate a list for result
# to create dfs we need to check the total with the target
# start with index-0, empty list as subset and 0 as total
# then if total is greater just return
# if equal append to sum the copy of subset
# then add the current item and pop on next
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return

            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res
