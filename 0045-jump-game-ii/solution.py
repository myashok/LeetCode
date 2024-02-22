class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = i = 0
        n = len(nums)
        if n == 1:
            return 0

        while True:
            if nums[i] + i >= n - 1:
                return ans + 1
                
            max_jump_index = i + 1
            for j in range(i + 2, i + nums[i] + 1):
                if nums[j] - (i - j + 1) > nums[max_jump_index] - (i - max_jump_index + 1):
                    max_jump_index = j
            ans += 1
            i = max_jump_index

