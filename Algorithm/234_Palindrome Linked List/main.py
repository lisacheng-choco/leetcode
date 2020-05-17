# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        ''' Solution 1
            Time Complexity: O(n)
            Space Complexity: O(n)
        '''
        forward, backward = '', ''
        while(head is not None):
            forward = forward + str(head.val)
            backward = str(head.val) + backward
            head = head.next
            
        return forward == backward
         
        
        ''' Solution 2
            Time Complexity: O(n)
            Space Complexity: O(1)
        ''' 
        # define a reverse function 
        def reverseLinkedList(node: ListNode):
            dummy, head = None, node
            first, second = dummy, head
            while(second is not None):
                nextSecond = second.next
                second.next = first
                first = second
                second = nextSecond
            return first
        
        slower, faster = head, head 
        while(faster is not None and faster.next is not None):
            slower = slower.next
            faster = faster.next.next
        middle = slower
        reverse = reverseLinkedList(middle) 
        
        while(reverse is not None):
            if(reverse.val != head.val):  
                return False   
            reverse = reverse.next
            head = head.next
        return True