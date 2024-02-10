class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, h = max(weights), sum(weights)
        def _is_this_capacity_possibile(capacity: int) -> bool:
            curr_weight_sum = 0
            cnt = 1
            for weight in weights:
                curr_weight_sum += weight
                if curr_weight_sum > capacity:
                    curr_weight_sum = weight
                    cnt += 1
                    if cnt > days:
                        return False
            return True

        while l < h:
            mid = (l + h) // 2
            if _is_this_capacity_possibile(mid):
                h = mid
            else:
                l = mid + 1

        return l
