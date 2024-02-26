from collections import deque
from typing import List

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        dq = deque([(0, 0, 0, 0)])  # (i, j, path_len, obstacles_used)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set([(0, 0, 0)])  # Initialize with starting point
        if k >= m + n - 2:
            return m + n - 2

        while dq:
            i, j, path_len, obstacles_used = dq.popleft()

            if i == m - 1 and j == n - 1:
                return path_len

            for dx, dy in directions:
                new_i, new_j = i + dx, j + dy

                if 0 <= new_i < m and 0 <= new_j < n:
                    new_obstacles = obstacles_used + grid[new_i][new_j]

                    if new_obstacles <= k and (new_i, new_j, new_obstacles) not in visited:
                        dq.append((new_i, new_j, path_len + 1, new_obstacles))
                        visited.add((new_i, new_j, new_obstacles))

        return -1

