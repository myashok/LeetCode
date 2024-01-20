class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr = [-10**5] + arr + [-10**5]
        stack = []
        ans = 0
        for i, n in enumerate(arr):
            while stack and arr[stack[-1]] > n:
                curr = stack.pop()
                ans += (curr - stack[-1])*(i-curr)*arr[curr]
            stack.append(i)
        return ans % (10**9+7)
