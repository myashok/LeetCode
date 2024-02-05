class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        total_count = defaultdict(int)
        for i in range(n):
            if tops[i] == bottoms[i]:
                total_count[tops[i]] += 1
            else:
                total_count[tops[i]] += 1
                total_count[bottoms[i]] += 1

        if total_count[tops[0]] <  total_count[bottoms[0]]:
            max_key = bottoms[0]
        else:
            max_key = tops[0]

        if total_count[max_key] < n:
            return -1
        
        return n - max(tops.count(max_key), bottoms.count(max_key))
        
