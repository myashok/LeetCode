import random

class Solution:
    def __init__(self, nums):
        # Store the input array
        self.nums = nums
        # Create a dictionary to map each number to its list of indices
        self.indices_map = defaultdict(list)
        for index, num in enumerate(nums):
            self.indices_map[num].append(index) 
    
    def pick(self, target):
        # Retrieve the list of indices for the target number
        indices = self.indices_map[target]
        # Randomly select and return one index from the list
        return random.choice(indices)

