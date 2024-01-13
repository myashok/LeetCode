class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1]*(n+1) 
        for i in range(n-1, -1, -1):
            ans[i] = ans[i+1]*nums[i]
        prev = 1
        for i in range(n):
            ans[i] = prev*ans[i+1]
            prev *= nums[i]

        return ans[:-1]
