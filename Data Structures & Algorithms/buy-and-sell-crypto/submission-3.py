class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: return 0

        profit = 0
        l, r = 0, 1
        while r <= len(prices)-1:
            if prices[r] < prices[l]:
                l = r
            else:
                profit = max(profit, prices[r] - prices[l])

            r += 1

        return profit

            
