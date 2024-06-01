class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        result = []
        for i, rows in enumerate(nums):
            for j, val in enumerate(rows):
                result.append((i + j, -i, val))
        return [el[2] for el in sorted(result)]
