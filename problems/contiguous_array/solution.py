class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mp = {}
        sum = 0
        ans = 0
        mp[0] = -1
        for index, num in enumerate(nums):
            sum += -1 if num == 0 else 1
            # print(sum, mp)
            if sum in mp:
                ans = max(ans, index - mp[sum])
            else:
                mp[sum] = index
        return ans

