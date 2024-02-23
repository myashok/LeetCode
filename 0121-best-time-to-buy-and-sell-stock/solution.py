class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        prev_min = 10**5
        for price in prices:
            if price > prev_min:
                ans = max(price-prev_min, ans)
            else:
                prev_min = price
        return ans
