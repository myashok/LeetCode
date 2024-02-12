class Solution:
    def is_possible_to_give(self, mid, candies, k):
        return sum(candy//mid for candy in candies) >= k

    def maximumCandies(self, candies: List[int], k: int) -> int:
        low = 0
        high = max(candies)
        while low < high:
            mid = (low + high + 1) // 2
            if self.is_possible_to_give(mid, candies, k):
                low = mid
            else:
                high = mid - 1
        return low
