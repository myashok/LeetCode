class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        
        ans = [0]*n
        child = [1]*n
        def dfs(u, p):
            for v in g[u]:
                if v != p:
                    dfs(v, u)
                    child[u] += child[v]
                    ans[u] += ans[v] + child[v]
        
        def dfs2(u, p):
            for v in g[u]:
                if v != p:
                    ans[v] = (ans[u] - child[v]) + (n - child[v])
                    dfs2(v, u)

        dfs(0, -1)
        dfs2(0, -1)
        return ans

                
