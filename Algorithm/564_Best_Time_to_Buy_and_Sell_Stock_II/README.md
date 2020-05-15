# 564_Best Time to Buy and Sell Stock II

## Link
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

## My Solution
### Solution 1
the total profit = the sum of local peaks - the sum of local valleys.
1. Initial empty List *valley* and *peak*
2. Initial a flag *isFindingValley* to keep we are going to by or sell, and *isFindingValley = True* is set in the beginning
3. Loop the prices 
    1. if *isFindingValley = True* and the i-1 element is smaller than i element, then put i-1 element in *valley* and swith *isFindingValley = False* 
    2. if *isFindingValley = False* and the i-1 element is greater than i element, then put i-1 element in *peak* and swith *isFindingValley = True* 
4.  The last emelemt in prices is not considered in the loop and there must be a paire of buy and sell. If the length of valley is greater than the length of peak, then add the last element to *valley*
5.  Teturn total profit

### Solution 2
1. Initialize *profit = 0*
2. loop prices, if ((i+1) element - i element) is > 0 then 
    > profit = profit +  ((i+1) element - i element)

## Notes
Python range()
> range（0， 5 -> [0, 1, 2, 3, 4] 

###### tags: `LeetCode` `learning`# template