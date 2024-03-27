class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        has_sum = defaultdict(int)
        has_sum[0] = 1
        ans = 0
        for num in nums:
            prefix_sum += num
            if prefix_sum - k in has_sum:
                ans += has_sum[prefix_sum - k]
            has_sum[prefix_sum] += 1
        return ans


