class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        a_xor_b = reduce(lambda x, y: x ^ y, nums)
        right_most_bit_num = a_xor_b  & -a_xor_b
        a, b = 0, 0
        for num in nums:
            if num & right_most_bit_num:
                a ^= num
            else:
                b ^= num
        return [a, b]
