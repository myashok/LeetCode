class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        n = len(number)
        for x in range(1, n):
            prev, cur = number[x-1], number[x]
            if prev == digit:
                last_ind = x-1
                if cur > prev:
                    ind = x - 1
                    return number[:ind] + number[ind+1:]
        else:
            if number[-1] == digit:
                return number[:-1]
            else:
                return number[:last_ind] + number[last_ind+1:]
            
