class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        k = 2
        freq = defaultdict(int)
        l = ans = 0
        for r, c in enumerate(s):
            freq[c] += 1
            while len(freq) > k:
                freq[s[l]] -= 1
                if freq[s[l]] == 0:
                    del freq[s[l]]
                l += 1
            else:
                if ans < r - l + 1:
                    ans = r - l + 1
        return ans
