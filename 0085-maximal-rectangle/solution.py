class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        height = [0] * n
        left = [0] * n
        right = [n] * n
        max_area = 0
        
        for i in range(m):
            cur_left, cur_right = 0, n
            # Update height array
            for j in range(n):
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0
            
            # Update left array
            for j in range(n):
                if matrix[i][j] == '1':
                    left[j] = max(left[j], cur_left)
                else:
                    left[j], cur_left = 0, j + 1
            
            # Update right array
            for j in range(n - 1, -1, -1):
                if matrix[i][j] == '1':
                    right[j] = min(right[j], cur_right)
                else:
                    right[j], cur_right = n, j
            
            # Update max area
            for j in range(n):
                max_area = max(max_area, height[j] * (right[j] - left[j]))
        
        return max_area

