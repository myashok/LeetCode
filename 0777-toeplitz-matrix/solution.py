class Solution:
    def isToeplitzMatrix(self, mat: List[List[int]]) -> bool:
        m = len(mat)
        n = len(mat[0])
        for t in range(m):
            j = 0
            i = t
            prev = mat[i][j]
            while  i < m and j < n:
                if mat[i][j] != prev:
                    return False
                i += 1
                j += 1
        
        for t in range(n):
            i = 0
            j = t
            prev = mat[i][j]
            while  i < m and j < n:
                if mat[i][j] != prev:
                    return False
                i += 1
                j += 1
        return True
