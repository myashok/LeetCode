class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""           
        count, l, r = Counter(t), 0, 0
        ans_l, ans_r,  n, total_count = 0, 10**5+1, len(s), len(t)
        while r < n:
            total_count -= (count[s[r]] > 0)
            count[s[r]] -= 1
            r += 1
            while total_count == 0:
                if ans_r - ans_l > r - l:
                    ans_r, ans_l = r, l
                total_count += (count[s[l]] == 0)
                count[s[l]] += 1   
                l += 1

        return "" if ans_r == 10**5+1 else s[ans_l: ans_r]
            
