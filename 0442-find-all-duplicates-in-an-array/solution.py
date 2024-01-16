class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = set()
        for i in range(n):
            nums[abs(nums[i])-1] = nums[abs(nums[i])-1] * -1

        for i in range(n):
            if nums[abs(nums[i])-1] > 0:
                ans.add(abs(nums[i]))
                
        return list(ans)



