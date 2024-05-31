class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        h = len(nums) - 1
        while l < h:
            mid = (l + h) // 2
            if (nums[l] <= nums[mid] and nums[l] <= target <= nums[mid]) or (nums[mid] <= nums[h] and (target <= nums[mid] or target > nums[h])):
                h = mid
            else:
                l = mid + 1
        return -1 if nums[l] != target else l
