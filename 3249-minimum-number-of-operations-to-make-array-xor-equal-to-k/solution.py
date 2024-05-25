class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        list_xor = 0
        for num in nums:
            list_xor = list_xor^num
        return bin(list_xor ^ k).count('1')

