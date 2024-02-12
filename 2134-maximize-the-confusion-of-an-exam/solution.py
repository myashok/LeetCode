class Solution:
    def maxConsecutiveAnswers(self, nums: str, k: int) -> int:
        max_freq = ans = l = 0
        freq = defaultdict(int)
        for r, num in enumerate(nums):
            freq[num] += 1
            max_freq = max(max_freq, freq[num])
            if r - l + 1 - max_freq > k:
               freq[nums[l]] -= 1
               l += 1
            else:
                ans = max(ans, r - l + 1) 
        return ans
