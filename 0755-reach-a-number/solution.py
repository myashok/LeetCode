class Solution:
    def reachNumber(self, target: int) -> int:
        n = 0
        s = 0
        target = abs(target)
        while s < target or (s - target) % 2 != 0:
            n += 1
            s += n
        return n

