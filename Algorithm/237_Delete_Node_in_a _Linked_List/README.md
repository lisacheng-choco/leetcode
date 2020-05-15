# 237_Delete Node in a Linked List 
## Link
https://leetcode.com/problems/delete-node-in-a-linked-list/


## My Solution [Link](https://github.com/lisacheng-choco/leetcode/blob/master/Algorithm/553_Delete_Node_in_a%20_Linked_List/main.py)
input param: node (not the tail)
1. assign the value of the node to the value of the next node.
2. assign the pointer of the node to the pointer of the next node.

**Time Complexity**: O(1)

## Notes: Linked List v.s. Array
Inserting a new element or deleting an element in an Array is expensive than Linked List because the existing elements have to be shifted.
Linked List: O(1), Array: O(n)
 
## Reference
- [Linked List | Set 1 (Introduction)](https://www.geeksforgeeks.org/linked-list-set-1-introduction/)
- [A Simple Introduction to Linked Lists for Data Scientists](https://towardsdatascience.com/a-simple-introduction-of-linked-lists-for-data-scientists-a71f0eb31d87)
- [用python實作linked-list](https://medium.com/@tobby168/%E7%94%A8python%E5%AF%A6%E4%BD%9Clinked-list-524441133d4d)


###### tags: `LeetCode` `learning`
