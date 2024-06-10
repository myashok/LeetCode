class Solution:
    def numOfWays(self, n: int) -> int:
        color_3 = 6
        color_2 = 6
        MOD = 10**9 + 7
        for i in range(1, n):
            temp_color_3 = color_3
            color_3 = (2 * color_3 + 2 * color_2) % MOD
            color_2 = (2 * temp_color_3 + 3 * color_2) % MOD

        return (color_3 + color_2) % MOD;
