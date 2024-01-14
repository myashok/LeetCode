class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low, high = 0, len(nums) - 1
        lower = higher = -1
        while low < high:
            mid = (low + high)//2
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid

        lower = low if (low < len(nums) and target == nums[low]) else lower
        
        low, high = 0, len(nums) - 1
        while low < high:
            mid = ceil((low + high)/2)
            if nums[mid] > target:
                high = mid - 1
            else:
                low = mid

        higher = low if low < len(nums) and target == nums[low] else higher
        return [lower, higher]
