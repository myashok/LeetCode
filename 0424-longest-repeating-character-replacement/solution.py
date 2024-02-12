class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = max_freq = l = 0
        freq = defaultdict(int)
        for r, c in enumerate(s):
            freq[c] += 1
            max_freq = max(max_freq, freq[c])
            if r - l + 1 - max_freq > k:
               freq[s[l]] -= 1
               l += 1
            else:
                ans = max(ans, r - l + 1)       
        return ans
