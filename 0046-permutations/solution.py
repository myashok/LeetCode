class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        def compute(curr_list, used):
            if len(curr_list) == n:
                ans.append(curr_list[:])
                return
            for i, num in enumerate(nums):
                if not used[i]:
                    used[i] = True
                    curr_list.append(num)
                    compute(curr_list, used)
                    used[i] = False
                    curr_list.pop()
        compute([], [False]*n)
        return ans
