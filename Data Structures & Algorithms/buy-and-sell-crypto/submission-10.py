class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0

        buyDay = 0
        for sellDay in range(len(prices)):
            if prices[buyDay] > prices[sellDay]:
                buyDay = sellDay
            
            maxP = max(prices[sellDay] - prices[buyDay], maxP)
        
        return maxP
            



