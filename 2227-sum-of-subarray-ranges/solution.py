class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        nums = [-10**10] + nums + [-10**10]
        stack = []
        smallest_sum = 0
        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] > num:
                curr = stack.pop()
                smallest_sum += (i - curr)*(curr - stack[-1])*nums[curr]
            stack.append(i)
            
        nums[0] = nums[-1] = 10**10
        stack = []
        largest_sum = 0
        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] < num:
                curr = stack.pop()
                largest_sum += (i - curr)*(curr - stack[-1])*nums[curr]
            stack.append(i)

        return largest_sum - smallest_sum

