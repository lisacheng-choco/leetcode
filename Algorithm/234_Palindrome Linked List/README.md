# 234_Palindrome Linked List

## Link
https://leetcode.com/problems/palindrome-linked-list/

## My Solution

### Solution 1
Translate Linked List values into a String.
1. Initial two String, *forward* and *backward*.
2. Loop the Node
	1. *forward*
		> forward = forward + Node.val
	2. *backward*
		> backward = Node.val + backward
3. Compare *forward* with *backward*, if they are the same then return True.

#### Time Complexity: O(n), Space Complexity: O(n)

### Solution 2
Find the middle of Linked List and we can get Head Linked List & Tail Linked List. Next, reverse Tail Linked and we can check if the value of Head Linked List and reversed Tail Linked List are the same.
1. Initial *slower* pointer and *faster* pointer
2. To find the middle of Linked List, *slower* takes one step and *faster* takes two steps in the loop. Stop the loop when *faster* or *faster.next* is None. 
	> slower = slower.next
	> faster = faster.next.next
	
In the end, *slower* can be take as the head of Tail Linked List.
3. Reverse Tail Linked List.
4. Check if node value of Head Linked List and reversed Tail Linked List are the same.

#### Time Complexity: O(n), Space Complexity: O(1)

## Notes
Palindrome 
- Wse String to concate the value of every node.
- Use 'reverse' to check if two Linked List are the same.

###### tags: `LeetCode` `learning`# template