from typing import List
from functools import lru_cache

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        # Convert stones into a set for faster lookup
        stones_set = set(stones)
        
        # Define a recursive function with memoization using lru_cache
        @lru_cache(maxsize=None)
        def solve(i, k):
            # If the current position is beyond the last stone, return False
            if i > stones[-1]:
                return False 
            
            # If the frog reaches the last stone, return True
            if i == stones[-1]:
                return True

            # Check if the frog can make a jump of size k from position i
            if i + k in stones_set:
                # Recursively check if the frog can reach the end with the same or incremented step
                if solve(i+k, k) or solve(i+k, k + 1):
                    return True
                # If the frog can make a decrementing jump, check for that too
                if k > 1 and solve(i+k, k - 1):
                    return True

            # If no jump is possible, return False
            return False
        
        # Start from the first stone with a jump of size 1
        return solve(0, 1)

