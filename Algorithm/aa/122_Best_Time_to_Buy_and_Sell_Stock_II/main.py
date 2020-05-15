class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ''' solution 1 '''
        valley = []
        peak = []
        isFindingValley = True
        j = 1
        while j < len(prices):
            if isFindingValley:
                if prices[j-1] < prices[j]:
                    valley.append(prices[j-1])
                    isFindingValley = False
            else:
                if prices[j-1] > prices[j]:
                    peak.append(prices[j-1])
                    isFindingValley = True
            j += 1
       
        if len(valley) > len(peak):
            peak.append(prices[len(prices)-1])
            
        return sum(peak) - sum(valley)
    
        ''' solution 2 '''
        profit = 0
        for i in range(len(prices)-1):
            if prices[i+1] - prices[i] > 0:
                profit += prices[i+1] - prices[i]
        return profit