class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        has_increasing = has_decreasing = None
        prev = -1
        for i in range(1, len(arr)):
            if arr[i] == arr[i-1]:
                return False
            
            elif arr[i] > arr[i-1]:
                
                if has_decreasing:
                    return False
                
                if not has_increasing:
                    has_increasing = True
            
            elif arr[i] < arr[i-1]:
                if not has_decreasing:
                    has_decreasing = True


        return has_increasing and has_decreasing



