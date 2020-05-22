# 141_Linked List Cycle

## Link
https://leetcode.com/problems/linked-list-cycle/

## My Solution
### Solution 1
Iterate linked list and mark the current Node as string 'visited'.

If Node.next.val == 'visited', then we find the cycle.

**Time Complexity:** O(N)

### Solution 2
1. Initial 2 pointers, 'slow' & 'fast'. 'slow' moves a step and 'fast' moves two steps at a time.
2. If 'fast' or 'fast.next' is Null, there is no cycle.
3. If 'fast' catch up with'slow', there is a cycle 

**Time Complexity:** O(N), Space Complexity: O(1)-> constant: 2 pointers

## Notes
Solution 2 - 判斷是否有cycle，想到倒追！

當快＆慢指標相差一個步伐時，快指標遲早會到追上慢指標。

###### tags: `LeetCode` `learning`