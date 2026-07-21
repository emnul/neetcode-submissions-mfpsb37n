class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        l, r = 0, 1

        while r < len(prices):
            currProfit = prices[r] - prices[l]
            maxProfit = max(currProfit, maxProfit)

            if prices[l] > prices[r]:
                l += 1
            elif prices[l] <= prices[r]:
                r += 1
            print(l,r)
            
        return maxProfit
