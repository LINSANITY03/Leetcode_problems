# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# to find if it is cyclic or not, we use hare and tortoise technique
# if a turtoise and hare run along a cuclic path the hare eventually catch up to turtoise

# we initiate slow and fast as head
# while there is fast and fast.next
# check if slow.next is fast.next.next


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
