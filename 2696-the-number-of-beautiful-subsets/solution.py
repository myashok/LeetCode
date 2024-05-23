class Solution:
    def beautifulSubsets(self, nums, k):
        freq_map = defaultdict(int)
        nums.sort()
        return self._count_beautiful_subsets(nums, k, freq_map, 0) - 1

    def _count_beautiful_subsets(self, nums, difference, freq_map, i):
        if i == len(nums):
            return 1
        total_count = self._count_beautiful_subsets(nums, difference, freq_map, i + 1)
        if freq_map[nums[i] - difference] == 0:
            freq_map[nums[i]] += 1
            total_count += self._count_beautiful_subsets(
                nums, difference, freq_map, i + 1
            )
            freq_map[nums[i]] -= 1  
        return total_count
