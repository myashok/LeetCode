class Solution:
    def canJump(self, nums: List[int]) -> bool:
        can_reach = 0
        for i, n in enumerate(nums):
            if i > can_reach:
                return False
            can_reach = can_reach if can_reach >  i + n else i + n
        return True


