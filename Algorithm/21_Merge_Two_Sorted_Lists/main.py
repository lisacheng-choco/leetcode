# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        first = l1
        second = l2
        dummy = ListNode()
        head = dummy
        while(first is not None and second is not None):
            if(first.val <= second.val):
                head.next = first
                first = first.next
                head = head.next
            else:
                head.next = second
                second = second.next
                head = head.next
                
        if(first is None):
            head.next = second
            
        if(second is None):
            head.next = first
            
        return dummy.next