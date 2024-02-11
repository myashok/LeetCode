class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        l = ans = odd_count = count = 0
        for num in nums:
            if num & 1:
                odd_count += num & 1
                count = 0
            while odd_count == k:
                odd_count -= nums[l] & 1
                count += 1
                l += 1
            ans += count
        return ans


