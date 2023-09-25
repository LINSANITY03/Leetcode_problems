# initiate list for result
# if the length is 1 just copy the list and return it
# for each and every number we need to add with other elements
# pop the first number
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []

        # base case
        if len(nums) == 1:
            return [nums[:]]  # nums[:] is a deep copy

        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            print('iterate', i)
            print('perms', perms)
            for perm in perms:
                perm.append(n)
            res.extend(perms)
            nums.append(n)
        return res


nums = [1, 2, 3]
print(Solution().permute(nums))
