class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMost(K):
            c = defaultdict(int)
            ans = l = 0
            for r in range(len(nums)):
                c[nums[r]] += 1
                while len(c) > K:
                    c[nums[l]] -= 1
                    if c[nums[l]] == 0:
                        del c[nums[l]]
                    l += 1
                ans += r - l + 1
            return ans
            
        return atMost(k) - atMost(k-1)
