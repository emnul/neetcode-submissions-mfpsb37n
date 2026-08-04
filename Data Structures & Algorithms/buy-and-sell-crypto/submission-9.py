class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxProfit = 0

        for r in range(len(prices)):
            curProfit = prices[r] - prices[l]
            print(curProfit)
            if prices[l] > prices[r]:
                l = r

            
            maxProfit = max(maxProfit, curProfit)
        return maxProfit

                
