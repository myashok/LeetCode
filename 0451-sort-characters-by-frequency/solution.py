from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = Counter(s)
        n = len(s)
        bucket = [[] for _ in range(n+1)]
        for c, freq in cnt.items():
            bucket[freq].append(c)
        
        ans = []
        for freq in range(n, -1, -1):
            for c in bucket[freq]:
                ans.append(c * freq)
        return "".join(ans)
