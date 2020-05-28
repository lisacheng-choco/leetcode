# 189_Rotate Array

## Link
https://leetcode.com/problems/rotate-array/

## My Solution

### Solution 1: Brute Method
Rotate 1 step in a time, so we need to rotate k times.
nums[i] = nums[i-1]
**Time Complexity: O(k*n), Space Complexity: O(1)** 

### Solution 2: Cycle
Rotatation problem just like a cycle. the last element's next is back to the first element.
** Time Complexity: O(n), Space Complexity: O(n+n) ** 

### Solution 3: Reverse for 3 Times
1. reverse [0, n-1]
2. reverse [0, k-1]
3. reverse [k, n-1]

*Reminder: k could be a number which is larger than n. If k=n, it means the outcome of rotation is the same as the original list*

**Time Complexity: O(n), Space Complexity: O(1)** 

## Notes

###### tags: `LeetCode` `learning`# template