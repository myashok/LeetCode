class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = Counter(nums)
        nums.clear()  
        for element, frequency in sorted(count.items()):
            nums.extend([element] * frequency)

