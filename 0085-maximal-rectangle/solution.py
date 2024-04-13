class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        height = [0] * n

        max_area = 0
        
        for i in range(m):
            st = []
            for j in range(n):
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0
                while st and height[st[-1]]>= height[j]:
                    h = height[st.pop()]
                    w = j - st[-1] - 1 if st else j
                    max_area = max(max_area, h*w)
                st.append(j)
            while st:
                h = height[st.pop()]
                w = n - st[-1] - 1 if st else n
                max_area = max(max_area, h*w)
        return max_area
