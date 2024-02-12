class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        k = len(set(nums))
        ans = l = 0
        count = defaultdict(int)
        n = len(nums)
        for r, num in enumerate(nums):
            count[num] += 1
            while len(count) == k:
                count[nums[l]] -= 1
                if count[nums[l]] == 0:
                    del count[nums[l]]
                ans += n - r
                l += 1

        return ans
