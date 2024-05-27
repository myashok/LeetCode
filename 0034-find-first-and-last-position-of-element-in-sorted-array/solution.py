from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_first(nums, target):
            l, h = 0, len(nums) - 1
            while l < h:
                mid = (l + h) // 2
                if nums[mid] < target:
                    l = mid + 1
                else:
                    h = mid
            return l if l < len(nums) and nums[l] == target else -1
        
        def find_last(nums, target):
            l, h = 0, len(nums) - 1
            while l < h:
                mid = (l + h + 1) // 2
                if nums[mid] > target:
                    h = mid - 1
                else:
                    l = mid
            return l if l < len(nums) and nums[l] == target else -1
        
        first_pos = find_first(nums, target)
        if first_pos == -1:
            return [-1, -1]
        last_pos = find_last(nums, target)
        return [first_pos, last_pos]

