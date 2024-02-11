from functools import cache
from typing import List

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        # Get the number of rows and columns in the grid
        row_count = len(grid)
        col_count = len(grid[0])

        # Define the recursive function with memoization using the cache decorator
        @cache
        def collect_max_cherries(curr_row, bot1_col_position, bot_2_col_position):
            # Base case: if we reach the bottom row, return 0
            if curr_row == row_count:
                return 0
                
            # Compute the number of cherries picked by both robots
            grid_picked_cherries = grid[curr_row][bot1_col_position]
            if bot1_col_position != bot_2_col_position:
                grid_picked_cherries += grid[curr_row][bot_2_col_position]

            # Initialize the maximum cherries collected from subproblems to 0
            max_cherries_by_subproblem = 0
            
            # Iterate over all possible moves for both robots
            for i in range(-1, 2):
                for j in range(-1, 2):
                    # Calculate the new positions of both robots after the move
                    new_bot1_col_position = bot1_col_position + i
                    new_bot2_col_position = bot_2_col_position + j
                    
                    # Check if the new positions are within the grid boundaries
                    if 0 <= new_bot1_col_position < col_count and 0 <= new_bot2_col_position < col_count:
                        # Update the maximum cherries collected from subproblems
                        max_cherries_by_subproblem = max(max_cherries_by_subproblem, collect_max_cherries(curr_row + 1, new_bot1_col_position, new_bot2_col_position))
            
            # Return the sum of cherries picked by both robots and the maximum cherries collected from subproblems
            return grid_picked_cherries + max_cherries_by_subproblem 

        # Call the recursive function with initial positions of both robots
        return collect_max_cherries(0, 0, col_count - 1)

