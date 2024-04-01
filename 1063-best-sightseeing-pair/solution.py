class Solution:
    def maxScoreSightseeingPair(self, arr: List[int]) -> int:
        n = len(arr)
        max_left_score = arr[0] + 0
        max_score = 0
        for i in range(1, n):
            max_score = max(max_score, max_left_score + arr[i] - i)
            max_left_score = max(max_left_score, arr[i] + i)
        return max_score
