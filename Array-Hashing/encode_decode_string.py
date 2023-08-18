# Design an algorithm to encode a list of strings to a string. The encoded string is then string is
# sent over the network and is decoded back to the original list of strings.

# class Solution:
#     """
#     @param: strs: a list of strings
#     @return: encodes a list of strings to a single string.
#     """
#     def encode(self, strs):
#         # write your code here

#     """
#     @param: str: A string
#     @return: decodes a single string to a list of strings
#     """
#     def decode(self, str):
#         # write your code here

class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs):
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    """
    @param: s: A string
    @return: decodes a single string to a list of strings
    """

    def decode(self, s):
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
        return res


input = ["lint", "code", "love", "you"]
soln_obj = Solution()
in_ = soln_obj.encode(input)
out_ = soln_obj.decode(in_)
print(in_)
print(out_)
