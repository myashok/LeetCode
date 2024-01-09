class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        ans = 0
        n = len(nums)
        mp = {num: True for num in nums }
        for j in range(0, n-1):
            if (nums[j] - diff in mp) and (nums[j] + diff  in mp):
                ans += 1
        return ans
