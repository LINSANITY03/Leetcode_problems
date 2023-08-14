from collections import defaultdict

# Solution 1

# we sort each str and append other similar to its value and current as key
# {key: value} ----> {current_sorted_str: list[compo1, compo2]}


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        anagram_map = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)

        return list(anagram_map.values())


# Solution 2

# for each word we initialize a list of 26 letter noting each index for alphabet letters
# indexing each letter, we convert letter into ascii value and subtract ascii value of letter a
# such that ascii("b") - ascii("a") = 86-85 = 1
# then we update key value as list of ascii and value as every word similar to its ascii list
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        str_dic = defaultdict(list)

        for s in strs:
            alpha = [0] * 26

            for each in s:
                alpha[ord(each) - ord('a')] += 1

            str_dic[tuple(alpha)].append(s)

        return str_dic.values()


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(Solution().groupAnagrams(strs))
