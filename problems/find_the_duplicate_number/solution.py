class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            count = 0
            mid = (high + low)//2
            for num in nums:
               if num <= mid:
                   count += 1
            if count > mid:
                high = mid
            else:
                low = mid + 1
        
        return low