from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        
        m, n = len(mat), len(mat[0])
        result = []
        upward = True
        
        i, j = 0, 0
        
        while len(result) < m * n:
            result.append(mat[i][j])
            if upward:
                if j == n - 1:
                    i += 1
                    upward = False
                elif i == 0:
                    j += 1
                    upward = False
                else:
                    i -= 1
                    j += 1
            else:
                if i == m - 1:
                    j += 1
                    upward = True
                elif j == 0:
                    i += 1
                    upward = True
                else:
                    i += 1
                    j -= 1
        
        return result

