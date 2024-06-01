class Solution(object):
    def largestIsland(self, grid):
        m, n = len(grid), len(grid[0])
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def dfs(i, j, index):
            stack = [(i, j)]
            area = 0
            while stack:
                ci, cj = stack.pop()
                if grid[ci][cj] != 1:
                    continue
                grid[ci][cj] = index
                area += 1
                for di, dj in direction:
                    ni, nj = ci + di, cj + dj
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                        stack.append((ni, nj))
            return area

        index = 2
        areas = {0: 0}
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    areas[index] = dfs(i, j, index)
                    index += 1
        
        max_area = max(areas.values())
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    connected_areas = set()
                    for di, dj in direction:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < m and 0 <= nj < n:
                            connected_areas.add(grid[ni][nj])
                    potential_area = 1 + sum(areas[k] for k in connected_areas)
                    max_area = max(max_area, potential_area)

        return max_area

