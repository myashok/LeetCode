class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        if len(stockPrices) <= 1:
            return 0
        if len(stockPrices) == 2:
            return 1
        stockPrices.sort(key = lambda x: (x[0], x[1]))
        price_diff = stockPrices[1][1] - stockPrices[0][1]
        day_diff = stockPrices[1][0] - stockPrices[0][0]
        ans = 1
        for i, [day, price] in enumerate(stockPrices[2:]):
            curr_price_diff = price - stockPrices[i+1][1]
            curr_day_diff = day - stockPrices[i+1][0]
            if curr_price_diff*day_diff  !=  price_diff*curr_day_diff:
                ans += 1
                price_diff = curr_price_diff
                day_diff = curr_day_diff
        
        return ans