class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        flagged_index = -1
        for i in range(n-2, -1, -1):
            # print(i, nums[i], nums[i+1])
            if nums[i] < nums[i+1]:
                flagged_index = i
                break
        # print(flagged_index)
        if flagged_index != -1:
            for i in range(n-1, flagged_index, -1):
                if nums[i] > nums[flagged_index]:
                    nums[i], nums[flagged_index] = nums[flagged_index], nums[i]
                    nums[flagged_index+1:] = sorted(nums[flagged_index+1:])
                    break
        else:
            nums.sort()

            


        
