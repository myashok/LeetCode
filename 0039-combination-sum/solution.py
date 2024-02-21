class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def solve(idx, target, chosen_nums):
            if target == 0 and chosen_nums:
                res.append(chosen_nums[:])
                return
            if target < 0:
                return
                
            for i in range(idx, len(candidates)):
                chosen_nums.append(candidates[i])
                solve(i, target - candidates[i], chosen_nums)
                chosen_nums.pop()

        solve(0, target, [])
        
        return res
            
