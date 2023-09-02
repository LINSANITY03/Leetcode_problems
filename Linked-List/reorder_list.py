# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# to reorder the listnode we need to reverse the latter half and put to half in two temp val
# after we can add the new node after every other node

# first we need to find the middle point so we make slow and fast var
# until fast reaches last we increment the slow
# after fast reaches last we have meet the middle point

# to reverse the latter half, we have pointer of slow.
# so we take node after slow i.e slow.next
# we used reverse_linked_list algorithm

# to merge two half we use temp as first and second half
# first.next is the second or the reverse one
# until we have value in second


class Solution:
    def reorderList(self, head: ListNode) -> None:
        # find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge two halfs
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
