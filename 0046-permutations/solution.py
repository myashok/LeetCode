class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def find_permutations(nums):
            if len(nums) == 0:
                return [[]]

            permutations = []

            for i in range(len(nums)):
                num = nums[i]
                remaining_nums = nums[:i] + nums[i+1:]
                for perm in find_permutations(remaining_nums):
                    permutations.append([num] + perm)
                    
            return permutations
    
        return find_permutations(nums)
