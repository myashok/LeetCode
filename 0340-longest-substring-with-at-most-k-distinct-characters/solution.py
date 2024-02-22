class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        r = ans = l = 0
        n = len(s)
        freq_count = defaultdict(int)
        for r, c in enumerate(s):
            freq_count[c] += 1
            while len(freq_count) > k and l <= r :
                freq_count[s[l]] -= 1
                if freq_count[s[l]] == 0:
                    del freq_count[s[l]]
                l += 1 
            ans = max(ans, (r-l+1))
            r += 1
        return ans


