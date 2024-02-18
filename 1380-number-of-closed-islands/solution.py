class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        parent = {}
        m = len(grid)
        n = len(grid[0])
        ans = 0

        def dfs(i, j):
            visited.add((i, j))
            diff = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dx, dy in diff:
                new_i = i + dx
                new_j = j + dy
                if (new_i >= 0 and new_i < m and new_j >= 0 and new_j < n) and (new_i, new_j) not in visited and grid[new_i][new_j] == 0:
                    parent[(new_i, new_j)] = (i, j)
                    dfs(new_i, new_j)
        
        def is_totally_surrounded_by_water(i, j):
            diff = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            node_to_look = set(parent.keys())
            for i, j in node_to_look:
                for dx, dy in diff:
                    new_i = i + dx
                    new_j = j + dy
                    if not (new_i >= 0 and new_i < m and new_j >= 0 and new_j < n):
                        return False

            return True

        for i in range(m):
            for j in range(n):
                if (i, j) not in visited and grid[i][j] == 0:
                    parent = dict()
                    parent[(i, j)] = -1
                    dfs(i, j)
                    if is_totally_surrounded_by_water(i, j):
                        ans += 1
        return ans


