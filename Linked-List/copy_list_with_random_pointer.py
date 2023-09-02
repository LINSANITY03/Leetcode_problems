
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

# in this solution we need to create a deep copy (new memory) of our old linked list
# the problem arise when we need to point to the node that has not been created/copied yet
# to do this we can create each node without any pointer then we can point accordingly

# the first we create a node and match it with previous node using hashmap
# we iterate the head node and we append the cur node as key and its cur.val as value

# in second half, we again iterate the head and in copy.next we search cur.next and cur.random from hashmap
# then put in copy.next and copy.random pointer then increment the list


class Solution:
    def copyRandomList(self, head: "Node") -> "Node":
        oldToCopy = {None: None}

        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next

        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next
        return oldToCopy[head]
