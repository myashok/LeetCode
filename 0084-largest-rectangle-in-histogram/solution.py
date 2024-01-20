class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        heights = [-10**5] + heights + [-10**5]
        stack = []
        ans = 0
        for i, height in enumerate(heights):
            while stack and heights[stack[-1]] > height:
                curr = stack.pop()
                area = (i - stack[-1] - 1)*heights[curr]
                if area > ans:
                    ans = area
            stack.append(i)
        return ans
