class Solution:
    def minEatingSpeed(self, piles: List[int], r: int) -> int:
        l, h = ceil(sum(piles)/r), max(piles)
        
        def _is_this_capacity_possibile(k: int) -> bool:
            hours = 0
            for pile in piles:
                hours += ceil(pile/k)

            return hours <= r


        while l < h:
            mid = (l + h) // 2
            if _is_this_capacity_possibile(mid):
                h = mid
            else:
                l = mid + 1

        return l
