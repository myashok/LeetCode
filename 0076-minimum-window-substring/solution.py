class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        count_t = Counter(t)
        required_count = len(t)
        ans_l, ans_r = 0, 10**5 + 1
        l = r = 0
        n = len(s)
        while r < n:
            required_count -= count_t[s[r]] > 0
            count_t[s[r]] -= 1
            while required_count == 0:
                if ans_r - ans_l > r - l:
                    ans_r, ans_l = r, l
                required_count += count_t[s[l]] == 0
                count_t[s[l]] += 1
                l += 1      
            r += 1

        return "" if ans_r == 10**5 + 1 else s[ans_l: ans_r + 1]

