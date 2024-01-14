class Solution:
  

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        m, n = len(matrix), len(matrix[0])
        high = m*n-1
        while low <= high:
            mid = (low + high) >> 1
            if matrix[mid//n][mid%n] == target:
                return True
                
            elif matrix[mid//n][mid%n] > target:
                high = mid-1
            
            else:
                low = mid+1

        return False
                