class Solution:
    class BIT:
        def __init__(self, size):
            self.size = size
            self.BIT = [0]*(size + 1)
        
        def update(self, idx, delta):
            while idx <= self.size:
                self.BIT[idx] += delta
                idx += idx & - idx
        
        def query(self, idx):
            sm = 0
            while idx > 0:
                sm += self.BIT[idx]
                idx -= idx & - idx
            return sm
        
    def countSmaller(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        bit = self.BIT(len(nums))
        ans = []
        for num in nums[::-1]:
            ans.append(bit.query(bisect.bisect_left(sorted_nums, num)))
            bit.update(bisect.bisect_left(sorted_nums, num) + 1, 1)
        return ans[::-1]


        
