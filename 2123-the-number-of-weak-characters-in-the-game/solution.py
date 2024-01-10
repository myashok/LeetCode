class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (-x[0], x[1]))
        ans = max_defence = 0
        for x in properties:
            if x[1] < max_defence:
                ans += 1
            else:
                max_defence = max(max_defence, x[1])
        return ans

