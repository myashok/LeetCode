from collections import Counter
from typing import List
import bisect

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        # Create a frequency dictionary for the ages
        ages_freq = dict(sorted(Counter(ages).items()))
        # Prefix sum array
        prefix_freq_sum = [0] * (len(ages_freq) + 1)
        ans = 0
        ages_freq_keys = list(ages_freq.keys())  
        # Iterate through each age in the frequency dictionary
        for i, (age, freq) in enumerate(ages_freq.items()):
            prefix_freq_sum[i + 1] = prefix_freq_sum[i] + freq
            lower_limit = age * 0.5 + 7
            youngest_age_index = bisect.bisect_right(ages_freq_keys, lower_limit)
            if youngest_age_index <= i:
                total_in_range = prefix_freq_sum[i + 1] - prefix_freq_sum[youngest_age_index]
                ans += freq * (total_in_range - 1)
        
        return ans


