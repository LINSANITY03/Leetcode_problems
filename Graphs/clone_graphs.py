"""
# Definition for a Node.
"""

# Node strucutre
# current value and its connected neighbors returns list or None


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# we cannot copy paste node as the questions says
# so we create a hashmap to create old and new node
# check if the node is given else return None
# then dfs(node) of whatever value it is
# check if the given node is in the hashMap then we have the new relative node and return it
# else create the new node by adding the previous node val to self.val
# then add it to the hashMap
# then we need to create its neighbours too...
# iterate to neighbours from the given node and append the dfs of those node to current(copy)
# then return copy


class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val)
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node) if node else None
