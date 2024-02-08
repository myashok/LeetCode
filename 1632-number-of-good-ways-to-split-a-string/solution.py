class Solution:
        def numSplits(self, s: str) -> int:
            length = len(s)
            if length == 1:  # never splittable
                return 0
            elif length == 2:  # always splittable
                return 1
            freq_ls = Counter(s)
            freq_rs = defaultdict(int)
            ans = 0
            for c in s:
                freq_ls[c] -= 1
                freq_rs[c] += 1
                if not freq_ls[c]:
                    del freq_ls[c]
                if len(freq_ls) == len(freq_rs):
                    ans += 1
            return ans
        
