# 560_Reverse Linked List

## Link
https://leetcode.com/problems/reverse-linked-list/

## My Solution [Link](https://github.com/lisacheng-choco/leetcode/blob/master/Algorithm/560_Reverse_Linked_List/main.py)
>Input: 1->2->3->4->5->NULL
>
>Output: 5->4->3->2->1->NULL
Switch the direction from the head to the end of node.
1. Initiate two flags, *'first = None'* and *'second = head'*
2. Iterate the list until *'second'* is None  
    1. Fisrt, create varable *'nextSecond = second.next'*.  
    2.  Assign *'second.next'* to *'first'* and  and assign *'first'* to *'nextSecond'*
3. Return *'first'*

## Notes

###### tags: `LeetCode` `learning`