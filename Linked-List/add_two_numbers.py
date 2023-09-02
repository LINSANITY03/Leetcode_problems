# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# this problem wants to sum of linked list node value in reverse order
# meaning instead of carry going to left it goes on right.

# first as a linked list solution we create a dummy node
# then while either of node has value or there is a carry we iterate the list
# if current node has value use it or else use 0
# perform the sum and check if there is carry
# to check we divide the sum by 10 to get carry and use modulo for value
# update the carry and listnode by using above var
# update pointer of cur to next node and both of list


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        cur = dummy

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            # update ptrs
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
