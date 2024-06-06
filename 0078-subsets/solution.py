class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(i, subset):
            if i == len(nums):
                res.append(subset[:])
                return
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1, subset)
            # decision NOT to include nums[i]
            subset.pop()
            dfs(i + 1, subset)

        dfs(0, [])
        return res
