class Solution:
    def jump(self, nums: List[int]) -> int:
        can_jump_upto = nums[0] + 0
        ans = 0
        i = 0
        n = len(nums)
        max_jump_index = 0
        while i < n:
            if i > can_jump_upto:
                i = max_jump_index
                max_jump_index = 0
                ans += 1
                can_jump_upto = i + nums[i]

            if i + nums[i] > max_jump_index + nums[max_jump_index]:
                max_jump_index = i

            i += 1
        return ans if n == 1 else ans + 1
