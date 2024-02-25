class Solution:
    class BinaryIndexedTree:
        def __init__(self, n):
            self.bit = [0] * (n + 1)
        
        def update(self, i, delta):
            while i < len(self.bit):
                self.bit[i] += delta
                i += i & -i
        
        def query(self, i):
            count = 0
            while i > 0:
                count += self.bit[i]
                i -= i & -i
            return count

    def reversePairs(self, nums):
        sorted_nums = sorted(nums)
        bit = self.BinaryIndexedTree(len(nums))
        count = 0
        for num in nums:
            count += bit.query(len(nums)) - bit.query(bisect.bisect_right(sorted_nums, 2 * num))
            bit.update(bisect.bisect_right(sorted_nums, num), 1)
        return count

# # Test cases
# nums1 = [1, 3, 2, 3, 1]
# nums2 = [2, 4, 3, 5, 1]

# print(reversePairs(nums1))  # Output should be 2
# print(reversePairs(nums2))  # Output should be 3

