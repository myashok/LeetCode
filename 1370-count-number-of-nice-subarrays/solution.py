from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        l = ans = odd_count = count = 0
        for num in nums:
            # If the number is odd, increment the odd_count
            if num & 1:
                odd_count += 1
                count = 0  # Reset the count for consecutive subarrays with k odd numbers
            while odd_count == k:
                # If odd_count equals k, we found a valid subarray
                odd_count -= nums[l] & 1  # Decrease odd_count when we move the left pointer
                count += 1  # Increase count for each valid subarray
                l += 1  # Move the left pointer to the right to find more subarrays
            ans += count  # Update the total count of subarrays
        return ans

