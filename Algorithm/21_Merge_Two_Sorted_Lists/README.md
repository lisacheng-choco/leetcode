# 21_Merge Two Sorted Lists

## Link
https://leetcode.com/problems/merge-two-sorted-lists/

## My Solution
Merge two sorted lists into New List
1. Initial two flag, *'first'* for the current node in *l1* and  *'second'* for the current node in *l2*
2. If *'first'* and *'second'* are not None, pick the smaller node as the next node of New List.
3. If out of one flag is None, then assign the other flag as the next node of New List.
4. Return New List.

## Notes

###### tags: `LeetCode` `learning`