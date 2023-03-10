from math import ceil
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        r = ceil(len(b) / len(a))
        for i in (r, r+1):
            temp = a*i
            if b in temp:
                return i
        return -1