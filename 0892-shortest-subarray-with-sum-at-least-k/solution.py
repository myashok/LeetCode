class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        ans = float('inf')
        dq = deque()
        dq.append((-1, 0))
        p_sum = 0
        for i, num in enumerate(nums):
            p_sum += num
            while dq and p_sum - dq[0][1] >= k:
                ans = min(ans, i - dq.popleft()[0])
            while dq and p_sum <= dq[-1][1]:
                dq.pop()     
            dq.append((i, p_sum))

        return ans if ans != float('inf') else -1
