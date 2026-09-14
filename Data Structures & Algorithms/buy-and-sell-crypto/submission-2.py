class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: return 0

        profit = 0
        l, r = 0, 1
        while r <= len(prices)-1:
            if prices[r] - prices[l] >= 0:
                profit = max(profit, prices[r] - prices[l])
            else:
                l = r

            r += 1

        return profit

            
