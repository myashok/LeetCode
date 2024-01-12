class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return -1 if k & 1 else nums[0]
        if k <= 1:
            return nums[k]

        if len(nums) < k:
            return max(nums)
                   
        elif len(nums) == k:
            return max(nums[:-1])
        else:
            return max(max(nums[:k-1]),nums[k])
        
