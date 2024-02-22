class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        def dfs(i):
            if arr[i] == 0:
                return True
            arr[i], arr_val = -1, arr[i]
            if i - arr_val >= 0 and arr[i - arr_val] != -1:
                if dfs(i - arr_val):
                    return True
            if i + arr_val < n and arr[i + arr_val] != -1:
                if dfs(i + arr_val):
                    return True
            return False
        
        return dfs(start)

