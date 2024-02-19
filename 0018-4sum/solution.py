class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = set()
        n = len(nums)
        nums.sort()
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] > (target//4) or nums[-1] < (target//4) :
                return ans
            for j in range(i+1,n):
                left = j + 1
                right = n - 1
                while left < right:
                    total = nums[i] + nums[left] + nums[right]+nums[j]
                    if total > target:
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        ans.add(tuple(sorted((nums[i], nums[left], nums[right],nums[j]))))
                        left += 1
                        right -= 1
        return ans
            
