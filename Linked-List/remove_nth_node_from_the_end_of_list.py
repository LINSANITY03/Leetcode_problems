# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# to remove the nth node from the end of the list
# we are using the dummy approach and right for the counter to nth node
# we are incrementing the right upto when n is 0

# then we are incrementing the left node to reach the require node
# we do this by incrementing left node upto right node reaches None state
# which fulfills the left node reaching require state

# afterwards we just edit the left.next node as left.next.next node
# and return dummy.next as we dont want to return the initial val:0 node set by dummy


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        # delete
        left.next = left.next.next
        return dummy.next
