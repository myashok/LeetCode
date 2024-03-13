class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        low = 0
        high = 10**9

        def is_possible(mid):
            last_taken = price[0]
            cnt = 1
            for i in range(1, len(price)):
                if price[i] - last_taken >= mid:
                    cnt += 1
                    last_taken = price[i]
                    if cnt >= k:
                        return True
            return False

        while low < high:
            mid = ceil((low + high)/2)
            if is_possible(mid):
                low = mid
            else:
                high = mid - 1

        return low
