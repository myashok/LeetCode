class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        int_n = int(n)
        if int_n <= 10:
            return str(int_n - 1)
        elif n.count('0') == length - 1 and n.count('1') == 1:
            return str(int_n - 1)
        
        elif n.count('9') == length:
            return str(int_n + 2)

        elif n[1:-1].count('0') == length - 2 and n.count('1') == 2:
            return str(int_n - 2)
        
        msd = n[:ceil(length/2)]
        if length & 1:
            new_n_candidates = [
                f"{msd}{msd[-2::-1]}",
                f"{int(msd)-1}{str(int(msd)-1)[-2::-1]}",
                f"{int(msd)+1}{str(int(msd)+1)[-2::-1]}"
            ]
        else:
            new_n_candidates = [
                f"{msd}{msd[::-1]}",
                f"{int(msd)-1}{str(int(msd)-1)[::-1]}",
                f"{int(msd)+1}{str(int(msd)+1)[::-1]}"
            ]
        min_diff = math.inf
        ans = math.inf
        for candidate in new_n_candidates:
            candidate_int = int(candidate)
            if abs(candidate_int - int_n) < min_diff and candidate_int != int_n:
                ans = candidate_int
                min_diff = abs(candidate_int - int_n)
            elif abs(candidate_int - int_n) == min_diff and candidate_int < ans:
                ans = candidate_int
        return str(ans)
