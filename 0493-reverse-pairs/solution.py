class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge(start, mid, end):
            left = nums[start:mid+1]
            right = nums[mid+1: end+1]
            left_len = len(left)
            right_len = len(right)
            count = l = r = 0
            while l < left_len and r < right_len:
                if left[l] <= 2 * right[r]:
                    l += 1
                else:
                    count += left_len - l
                    r += 1
                    
            
            l = r = 0
            k = start
            while l < left_len and r < right_len:
                if left[l] <= right[r]:
                    nums[k] = left[l]
                    l += 1
                else:
                    nums[k] = right[r]
                    r += 1
                    
                k += 1
            while l < left_len:
                nums[k] = left[l]
                k += 1
                l += 1
            
            while r < right_len:
                nums[k] = right[r]
                k += 1
                r += 1
            # print(left, right, count)       
            return count
            
            
            
        def mergeSort(start, end):
            if start >= end:
                return 0
            else:
                mid = (end+start)//2
                ans = 0
                ans += mergeSort(start, mid)
                ans += mergeSort(mid+1, end)
                ans += merge(start, mid, end)
                return ans
            e
                
        
        ans =  mergeSort(0, len(nums)-1)
        # print(nums)
        return ans    
            
