class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = 10**6
        nums.sort()
        n = len(nums)

        if sum(nums[:3]) >= target:
            return sum(nums[:3])

        if sum(nums[-3:]) <= target:
            return sum(nums[-3:])   

        for i in range(n-2):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            j, k = i + 1, n - 1
            while j < k:
                three_sum = nums[i] + nums[j] + nums[k]
                if three_sum == target:
                    return three_sum
                if abs(three_sum - target) < abs(ans - target):
                   ans = three_sum
                elif three_sum < target:
                    j += 1
                else:
                    k -= 1

        return ans
