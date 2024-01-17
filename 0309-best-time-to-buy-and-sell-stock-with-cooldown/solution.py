class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0

        have_stock_at_index = [0]*n # represent that at given index I have a stock
        no_stock_at_index= [0]*n # represent that at given index I don't have a stock
        have_stock_at_index[0] = -prices[0]
        no_stock_at_index[0] = 0
        
        for i in range(1, n):
            have_stock_at_index[i] = max(no_stock_at_index[i-2] - prices[i], have_stock_at_index[i-1])
            no_stock_at_index[i] = max(prices[i] + have_stock_at_index[i-1], no_stock_at_index[i-1])

        return no_stock_at_index[n-1]

