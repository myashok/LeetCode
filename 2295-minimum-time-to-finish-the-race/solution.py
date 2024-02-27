class Solution:
    def minimumFinishTime(
        self, tires: List[List[int]], changeTime: int, numLaps: int
    ) -> int:
        without_change = [[math.inf] * 20 for _ in range(len(tires))]
        for i, (f, r) in enumerate(tires):
            without_change[i][1] = f
            for j in range(2, 20):
                without_change[i][j] = without_change[i][j - 1] * r
                if without_change[i][j] >= 10**7:
                    break
            for j in range(2, 20):
                without_change[i][j] += without_change[i][j - 1]
                if without_change[i][j] >= 10**7:
                    break

        

        dp = [math.inf] * (numLaps + 1)

        for i in range(1, numLaps + 1):
            if i < 20:
                for j in range(len(tires)):
                    dp[i] = min(dp[i], without_change[j][i])

            for j in range(i//2, i):
                if dp[j] != math.inf and dp[i-j] != math.inf:
                    dp[i] = min(dp[i], dp[j] + changeTime + dp[i - j])

        return dp[numLaps]

