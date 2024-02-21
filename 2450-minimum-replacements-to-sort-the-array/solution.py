class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        last = nums[n - 1]
        ans = 0
        # Traverse the array in reverse order
        for i in range(n - 2, -1, -1):
            if nums[i] > last: 
                if nums[i] % last:
                    num_elements = nums[i]//last + 1
                    last = nums[i]//num_elements
                    ans += num_elements - 1
                else:
                    ans += nums[i]//last - 1

            else:
                last = nums[i]  # Update 'last' without replacement
        
        return ans  # Return the total number of operations
