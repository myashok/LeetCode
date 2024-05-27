class Solution:
    def maximumSwap(self, num: int) -> int:
        s_num_list = list(str(num))
        ans = num
        for i in range(len(s_num_list)):
            for j in range(i + 1, len(s_num_list)):
                s_num_list[i], s_num_list[j] = s_num_list[j], s_num_list[i]
                ans = max(ans, int("".join(s_num_list)))
                s_num_list[i], s_num_list[j] = s_num_list[j], s_num_list[i]
        return ans
