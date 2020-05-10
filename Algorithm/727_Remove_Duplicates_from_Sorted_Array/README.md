# 727_Remove Duplicates from Sorted Array

## Link
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

## My Solution [Link](https://github.com/lisacheng-choco/leetcode/blob/master/Algorithm/727_Remove_Duplicates_from_Sorted_Array/main.py)
:::info
Prerequisite
1. Space Complexity: O(1)
2. Remove the duplicates in-place
:::

1. initialize two pointers: i=0 -> slower runner; j=1 -> fast runner
2. loop the list
    1. if i^th^ element != j^th^ element, assign i+1^th^ element to j^th^ element and increase j by 1.
    2. if i^th^ element = j^th^ element, increase j by 1
3. return i+1 (the length of non-duplicated emements)

## Notes
**Time Complexity**: O(N)

###### tags: `LeetCode` `learning`