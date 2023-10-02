# check of edge cases as the string can be 0, just return empty list
# first we need to create a dict or number to char
# then intiailize a empty list from returning output
# if there is any digits present in the string, intialize the backtrack with index 0 and empty string
# if the length of subset is equal to length of digits, return the copy of subset
# for each value in dictionary of the number to char
# backtrack with +1 in the index such that it points to next element and add the current to subset
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:

        if len(digits) == 0:
            return []

        digitToChar = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        res = []

        def backtrack(i, cur):

            if len(cur) == len(digits):
                res.append(cur[::])
                return

            for c in digitToChar[digits[i]]:
                backtrack(i + 1, cur + c)

        if digits:
            backtrack(0, "")

        return res


digits = "23"
print(Solution().letterCombinations(digits))
