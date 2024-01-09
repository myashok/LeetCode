class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        ans = 0
        group_size = 1
        n = len(grades)
        while True:
            if group_size >= n:
                ans += (group_size == n)
                break
            ans += 1
            n -= group_size
            group_size += 1
                     
        return ans