class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: return 0

        profit = 0

        for l in range(len(prices)-1):
            r = l+1
            # print("prices[l]: ", prices[l])
            # print("prices[r]: ", prices[r])
            # print("r: ", r)
            while r <= len(prices)-1 and prices[r] - prices[l] > 0:
                profit = max(profit, prices[r] - prices[l])
                r += 1
            
            if r < len(prices)-1 and prices[r] < prices[l]:
                l = r


        return profit

            
