class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        map = dict()
        start = 0
        max_len = 0
        for i, chr in enumerate(s):
            if chr in map:
                start = max(start, map[chr] + 1)
            map[chr] = i
            max_len = max(max_len, (i - start) + 1)
            
        return max_len
