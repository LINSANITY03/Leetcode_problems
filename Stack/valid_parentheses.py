# O(n)

# create hashmap with opposite parenthesis as key and positive as value
# create loop with each element check in hashMap
# if it is in stack then check if last element is equal to positive value
# else return false
# if there are value in stack then return stack

class Solution:
    def isValid(self, s: str) -> bool:

        hashMap = {')': '(', '}': '{', ']': '['}
        stack = []

        for c in s:
            if c in hashMap:
                print('stack', stack)
                print('c', c)
                if stack and stack[-1] == hashMap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False


s = "({[]})"
print(Solution().isValid(s))
