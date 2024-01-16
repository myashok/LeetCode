class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        min_buy_price = prices[0] + fee
        ans = 0
        for p in prices:
            if p > min_buy_price:
                ans += p - min_buy_price
                min_buy_price = p
            elif p + fee < min_buy_price:
                min_buy_price = p + fee

        return ans




