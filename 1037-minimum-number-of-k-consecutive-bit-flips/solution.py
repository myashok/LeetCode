class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        q = deque()
        res = 0
        for i, num in enumerate(nums):
            if num == (len(q) % 2):
                res += 1
                q.append(i + k - 1)
            if q and q[0] <= i:
                q.popleft()
        return -1 if q else res



        
