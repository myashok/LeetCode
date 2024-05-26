class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def solve(path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                if path.count(nums[i]) < nums.count(nums[i]):
                    path.append(nums[i])
                    solve(path)
                    path.pop()
        res = []
        solve([])
        return res
