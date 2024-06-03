
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        ans = 0
        n = len(nums)

        @lru_cache(None)
        def solve(i, curr_sum):
            if i == n:
                return curr_sum == target
            return solve(i + 1, curr_sum - nums[i]) + solve(i + 1, curr_sum + nums[i])
        return solve(0, 0)


