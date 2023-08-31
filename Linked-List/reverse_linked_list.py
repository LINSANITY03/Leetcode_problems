# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# before we reverse the linked list we need to make sure the last node is none
# so we first start out with prev value as none and current value as head
# while there is current value
# first we need to store all the curr.next value(except the first one) on a temp var
# then we need to make the first value has next as none {val: 1, next: None}
# so we put curr.next = prev
# then previous value is the current value ({val:1, next:None})
# curr = temp{val:2 , next:ListNode{val:3, next:...}}
# we need to add prev value to current and set it to prev value and wait for curr.next as temp


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev


head = [1, 2, 3, 4, 5]
print(Solution().reverseList(head))
