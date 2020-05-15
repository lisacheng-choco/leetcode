# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # Solution: Iterative
        first, second = None, head
        while(second is not None):
            nextSecond = second.next
            second.next = first
            first = second
            second = nextSecond
        return first
        
        
        