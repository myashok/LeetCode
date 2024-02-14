class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive_number = []
        negative_number = []
        for num in nums:
            if num > 0:
                positive_number.append(num)
            else:
                negative_number.append(num)
        nums[0 : len(positive_number) * 2 : 2] = positive_number
        nums[1 : len(negative_number) * 2 : 2] = negative_number
        return nums
