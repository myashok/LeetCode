class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        start = ans = 0
        mp = defaultdict(int)
        for end in range(len(nums)):
            mp[nums[end]] += 1
            while mp[nums[end]] > k:
                mp[nums[start]] -= 1
                start += 1
            else:
                if end - start + 1 > ans:
                    ans = end - start + 1
        
        return ans
        
