class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == '1':
            return False
        n = len(s)
        end = minJump
        reach = [False]*n
        reach[0] = [False]*True
        for i in range(n):
            if reach[i]:
                start, end = max(i + minJump, end), min(i + maxJump + 1, n)
                for j in range(start, end):
                    if s[j] == '0':
                        reach[j] = True
                if end == n:
                    return reach[-1]
        return reach[-1]
