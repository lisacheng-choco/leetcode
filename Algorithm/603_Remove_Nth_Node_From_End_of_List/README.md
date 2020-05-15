# 603_Remove Nth Node From End of List

## Link

https://leetcode.com/problems/remove-nth-node-from-end-of-list/

## My Solution [Link](https://github.com/lisacheng-choco/leetcode/blob/master/Algorithm/603_Remove_Nth_Node_From_End_of_List/main.py)

nth from end of list = (Length - n + 1) from beginning of list, and Length is the length of list.
(head is 1th from beginning of list)

0. Add dummy node to the head of list.
1. Get *Length* by iterating the list.
2. Get the previous node we want to remove by locating at (Length-n)th in list.
3. Assign previous node's next node to its next*2 node.

## Notes

###### tags: `LeetCode` `learning`