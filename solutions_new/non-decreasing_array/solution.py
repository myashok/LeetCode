class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0
        prev = nums[0]
        for i in range(1, len(nums)):
            if prev > nums[i]:
                count += 1
                if count > 1:
                    return False
                if not (i - 2 < 0 or nums[i-2] <= nums[i]):
                    continue
                           
            prev = nums[i]
        return True
        