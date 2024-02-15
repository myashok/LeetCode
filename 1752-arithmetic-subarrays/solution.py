class Solution:
    def checkArithmeticSubarrays(
        self, nums: List[int], l: List[int], r: List[int]
    ) -> List[bool]:
        ans = []

        def check(i, j):
            arr = nums[i : j + 1]
            mn = min(arr)
            mx = max(arr)
            num_to_pos_set = set(arr)

            min_max_diff = mx - mn
            elements_count = j - i
            if min_max_diff % (elements_count) != 0:
                return False
            else:
                diff = min_max_diff // (elements_count)

            for k in range(1, elements_count):
                if not (mn + k * diff in num_to_pos_set):
                    return False

            return True

        for i, j in zip(l, r):
            ans.append(check(i, j))

        return ans

