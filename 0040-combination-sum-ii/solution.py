from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        result = []
        comb = []
        def solve(start, remain):
            
            if remain == 0:
                result.append(comb[:])
                return
            if remain < 0 or start >= n:
                return
            if candidates[start] <= target:
                # Choose the current element
                comb.append(candidates[start])
                solve(start + 1, remain - candidates[start])
                comb.pop()

            # Skip duplicates and not choose the current element
            while start + 1 < n and candidates[start] == candidates[start + 1]:
                start += 1
            solve(start + 1, remain)
        
        solve(0, target)
        return result

