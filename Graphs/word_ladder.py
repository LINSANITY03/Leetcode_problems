import collections

# main logic is to create a adjacent list of similar words to reduce the search time
# first we create a dictionary and add each combination of similar word to the list
# {'*ot': ['hot', 'dot', 'lot'],
# 'h*t': ['hot', 'hit'],
# 'ho*': ['hot'],
# 'd*t': ['dot'],
# 'do*': ['dot', 'dog'],
# '*og': ['dog', 'log', 'cog'],
# 'd*g': ['dog'],
# 'l*t': ['lot'],
# 'lo*': ['lot', 'log'],
# 'l*g': ['log'],
# 'c*g': ['cog'],
# 'co*': ['cog'],
# '*it': ['hit'],
# 'hi*': ['hit']})
# after creating the combination hashmap we need to create a set for visited word
# then we create a queue to run the loop with beginword initialized
# from queue we need to popleft and compare to endword
# if equal return result else
# search the pattern in the hashmap add the word to the queue and visited
# until all string are visited or condition is met


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList:
            return 0

        nei = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                nei[pattern].append(word)
        print(nei)
        visit = set([beginWord])
        q = collections.deque([beginWord])
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)
            res += 1
        return 0


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
print(Solution().ladderLength(beginWord, endWord, wordList))
