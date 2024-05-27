class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}
        def solve(u, p, c):
            color[u] = c
            for v in graph[u]:
                if v != p:
                    if v not in color:
                        if not solve(v, u, 1-c):
                            return False
                    elif color[v] == c:
                        return False
            return True
        for v in range(len(graph)):
            if v not in color and not solve(v, -1, 0):
                return False
        return True
