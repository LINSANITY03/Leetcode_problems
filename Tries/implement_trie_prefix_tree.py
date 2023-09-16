# initiate the TrieNode class with dictionaries and bool
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

# init the Tries with empty TrieNode

# set root as current and for each letter in word we use the loop
# if the current element is in the current children
# if there are no children initiate a empty TrieNode
# else move the pointer and after the loop finishes set the endOfWord bool true

# searching is similar as we need to iterate until we have the bool true else false

# start with is similar just loop until elements


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.endOfWord

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True
