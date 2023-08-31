# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# first we initiate a empty linkedlist as dummy node and a tailnode referenced to it.
# dummy will act as head and tail as temp linkedlist to update as we go
# if the val of list1 is less than list2 we can add list1 to our linkedlist and remove from list1
# tail.next = list1 adds our node to dummy and list1 = list1.next removes it from list1
# same for list2
# after loop if there are some values in list1 or list2
# we will add to our pointer since it is already sorted
# then we return dummy.next as dummy saves as the node from head to tail and
# .next so that we will not return initial val=0 node


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 or list2
        return dummy.next


list1 = [1, 2, 4]
list2 = [1, 3, 4]
print(Solution().mergeTwoLists(list1, list2))
