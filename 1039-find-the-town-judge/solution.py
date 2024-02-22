class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        is_trusting = [0]*n
        is_trusted = [0]*n
        for x, y in trust:
            is_trusting[x-1] += 1 
            is_trusted[y-1] += 1 
        try:
            index = is_trusted.index(n-1) + 1
            return index if not is_trusting[index-1] else -1
        except ValueError as v:
            return -1
