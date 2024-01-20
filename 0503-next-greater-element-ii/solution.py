class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = nums + nums[:-1]
        ans = [-1] * n
        stack = []

        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] < num:
                curr = stack.pop()
                ans[curr] = num

            if i < n:
                stack.append(i)

        return ans

