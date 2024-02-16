from itertools import combinations
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        N = n // 2
        left_sum = defaultdict(list)
        right_sum = defaultdict(list)
        
        def get_sum(left_arr, right_arr):
            lsm_dict = defaultdict(list)
            rsm_dict = defaultdict(list)
            for k in range(N+1):
                sm = 0
                for c in combinations(left_arr, k):
                    lsm_dict[k].append(sum(c))
                sm = 0
                for c in combinations(right_arr, k):
                    rsm_dict[k].append(sum(c))

            return lsm_dict, rsm_dict

        left_sums, right_sums = get_sum(nums[:N], nums[N:])
        total = sum(nums)
        half = total // 2
        ans = float('inf')
        for k in range(N):
            left = left_sums[k] 
            right = right_sums[N-k]
            right.sort()
            for x in left:
                r = half - x
                p = bisect.bisect_left(right, r)
                for q in [p, p-1]:
                    if -1 < q < len(right):
                        left_ans_sum = x + right[q]
                        if left_ans_sum == half:
                            return total - 2*half
                        right_ans_sum = total - left_ans_sum
                        diff = abs(left_ans_sum - right_ans_sum)
                        ans = min(ans, diff) 
        return ans
        
