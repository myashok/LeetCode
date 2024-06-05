class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        arr = [0] * (max(right for (val, left, right) in trips) + 1)
        for (val, left, right) in trips:
            arr[left]  += val
            arr[right] -= val
        
        curr = 0
        for i in range(len(arr)):
            curr += arr[i]
            if curr > capacity:
                return False
        
        return True
