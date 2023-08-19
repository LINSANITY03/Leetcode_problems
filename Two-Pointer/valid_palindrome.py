# O(N)

# if the char is alpha numeric add lower value into string
# reverse the string and compare with original
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([c for c in s if c.isalnum()]).lower()
        if s == s[::-1]:
            return True
        return False

# using two pointers
# initalize the pointer pointing initial and last value
# check if element is alphanum else increase the pointer
# after having valid item in both pointer, check if their lower value is equal


class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.alphanum(s[l]):
                l += 1
            while l < r and not self.alphanum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

    # Could write own alpha-numeric function
    def alphanum(self, c):
        return (
            ord("A") <= ord(c) <= ord("Z")
            or ord("a") <= ord(c) <= ord("z")
            or ord("0") <= ord(c) <= ord("9")
        )


s = "A man, a plan, a canal: Panama"
print(Solution().isPalindrome(s))
