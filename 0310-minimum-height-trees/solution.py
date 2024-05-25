class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        degree = [0]*n
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
            degree[u] += 1
            degree[v] += 1
        
        leaves = deque()
        for i in range(n):
            if degree[i] == 1:
                leaves.append(i)
        
        remaining_nodes = n
        while remaining_nodes > 2:
            leaves_size = len(leaves)
            remaining_nodes -= leaves_size
            for _ in range(leaves_size):
                leaf = leaves.popleft()
                for u in g[leaf]:
                    degree[u] -= 1
                    if degree[u] == 1:
                        leaves.append(u)
        return list(leaves)

