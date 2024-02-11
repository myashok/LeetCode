class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        i = count = res = 0
        for j in range(len(nums)):
            if nums[j] == 1:
                goal -= 1
                count = 0
            while goal < 0:
                goal += nums[i]
                i += 1

            while goal == 0 and i <= j:
                goal += nums[i]
                i += 1
                count += 1
                if i > j - goal + 1:
                    break

            res += count
        return res
