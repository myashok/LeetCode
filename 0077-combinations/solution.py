class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def solve(current_num, chosen_count, path):
            if chosen_count == k:
                res.append(path[:])
                return
            if current_num > n:
                return
            path.append(current_num)
            solve(current_num + 1, chosen_count + 1, path)
            path.pop()
            solve(current_num + 1, chosen_count , path)
        res = []
        solve(1, 0, [])
        return res

