# if length of first word is greater than second word then it cannot be permutation string
# then we state two 26 index list for bit manipulation checking as s1Count and s2Count
# first we match the first word length word to second word using ascii value of ele - ascii('a')
# it can give us the alphabet number of the element
# we need to check how much matches there was
# max is 26 then it is right return true
# else we need to add next index ele as release our initial ele making the window length == s1
# do until if matches == 26 or loop finishes.
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26
        print('initial s1count', s1Count)
        print('initial s2count', s2Count)
        print('-----------------------------------------')
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord("a")] += 1
            s2Count[ord(s2[i]) - ord("a")] += 1

        print('after s1 loop', s1Count)
        print('after s2 loop', s2Count)
        print('-----------------------------------------')

        matches = 0
        for i in range(26):
            matches += 1 if s1Count[i] == s2Count[i] else 0
        print('initial matches', matches)

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord("a")
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord("a")
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26


s1 = "ab"
s2 = "eidbaooo"
print(Solution().checkInclusion(s1, s2))
