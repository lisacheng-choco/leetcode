# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        length = 0
        # add a dummy to the beginnig of head for dealing with some cases, including a list with one node
        dummy = ListNode()
        dummy.next = head
        target = dummy
        # get the length of list by iterating the list
        while(target.next is not None):
            length += 1
            target = target.next
        
        # get the previous node, 'first', of the node we want to remove
        first = dummy
        for i in range(length - n):
            first = first.next
        first.next = first.next.next
        return dummy.next