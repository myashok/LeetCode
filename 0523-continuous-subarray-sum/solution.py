class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mod_num = {0:-1}
        mod = 0
        for i in range(len(nums)):
            mod = (mod + nums[i]) % k
            if mod in mod_num:
                if i - mod_num[mod] >= 2:
                    return True
            else:
                mod_num[mod] = i

        return False



