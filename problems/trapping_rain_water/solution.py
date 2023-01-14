class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_largest = [0]*n
        left_largest[0] = height[0]
        
        right_largest = [0]*n
        right_largest[-1] = height[-1]
        
        for i in range(1, n):
            left_largest[i] = max(left_largest[i-1], height[i])
            right_largest[-i-1] = max(right_largest[-i], height[-i-1])

        ans = 0 
        for i in range(1, n-1):
            ans += max(min(left_largest[i-1], right_largest[i+1]) - height[i], 0)
        
        return ans