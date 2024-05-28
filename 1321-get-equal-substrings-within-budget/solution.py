class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        cost = [0] * (n + 1)
        ans = 0

        # # Compute the prefix sum of costs
        # for i in range(1, n + 1):
        #     cost[i] = abs(ord(s[i - 1]) - ord(t[i - 1])) + cost[i - 1]

        # Use binary search to find the maximum length substring within the maxCost
        for i in range(1, n + 1):
            cost[i] = abs(ord(s[i - 1]) - ord(t[i - 1])) + cost[i - 1]
            if cost[i] > maxCost:
                prev_index = bisect.bisect_left(cost[:i+1], cost[i] - maxCost)
                ans = max(ans, i - prev_index)
            else:
                ans = max(ans, i)

        return ans
