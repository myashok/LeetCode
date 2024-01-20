class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        n = len(nums)    
        for i in range(n-2):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i-1]:
                continue

            j, k = i + 1, n - 1
            while j < k:
                three_sum = nums[i] + nums[j] + nums[k]
                if three_sum == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1    
                    while j < k and nums[j] == nums[j-1]:
                        j += 1

                elif three_sum < 0:
                    j += 1
                else:
                    k -= 1

        return ans

            
