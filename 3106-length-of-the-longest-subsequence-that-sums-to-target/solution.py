class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        dp = {0: 0}
        for num in nums:
            new_dp = {}
            for sum_num, len_sub in dp.items():
                sum_num += num 
                if sum_num <= target:
                    if sum_num not in dp or len_sub >= dp[sum_num]:
                        new_dp[sum_num] = len_sub + 1
            dp |= new_dp
        return dp.get(target, -1)
