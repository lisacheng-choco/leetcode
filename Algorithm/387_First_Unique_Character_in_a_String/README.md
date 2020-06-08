# 387_First Unique Character in a String

## Link
https://leetcode.com/problems/first-unique-character-in-a-string/

## My Solution
### Solution 1: Hash Table
1. Create a hash table by declaring a dictionary to store character and its count. Key is the character and value is its count number.
2. Iterate the key in the dictionary and find the frist key with count=1.
3. Return the index by using *index* function to get the index of the alphabet first meet.

### Solution 2: Pre-defined Alphabets
1. Store the index which its character is non-repeating by iterating alphabets from 'a' to 'z'

## Notes
solution 1's *dictionary* can be replaced by *enumerate*.
> seq = ['one', 'two', 'three']

> for i, element in enumerate(seq):

> 	print i, element

###### tags: `LeetCode` `learning`# template