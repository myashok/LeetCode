class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def solve(a, b):
            if len(a) > len(b):
                return solve(b, a)
            a_len, b_len = len(a), len(b)
            low, high = 0, a_len
            while low <= high:
                partition_a = (low + high) // 2
                partition_b = (a_len + b_len + 1) // 2 - partition_a
                max_left_a = -math.inf if partition_a == 0 else a[partition_a - 1]
                min_right_a = math.inf if partition_a == a_len else a[partition_a]
                max_left_b = -math.inf if partition_b == 0 else b[partition_b - 1]
                min_right_b = math.inf if partition_b == b_len else b[partition_b]
                if max_left_a <= min_right_b and max_left_b <= min_right_a:
                    if (a_len + b_len) & 1:
                        return max(max_left_a, max_left_b)
                    else:
                        return (
                            max(max_left_a, max_left_b) + min(min_right_a, min_right_b)
                        ) / 2
                elif max_left_a > min_right_b:
                    high = partition_a - 1
                else:
                    low = partition_a + 1

        return solve(nums1, nums2)

