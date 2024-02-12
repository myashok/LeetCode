class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        max_freq = l = 0
        freq = defaultdict(int)
        for r, num in enumerate(nums):
            freq[num] += 1
            max_freq = max(max_freq, freq[num])
            while r - l + 1 - max_freq > k:
               freq[nums[l]] -= 1
               l += 1       
        return max_freq

