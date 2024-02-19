class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        target = len(graph) - 1
        def dfs(u, path):
            if u == target:
                ans.append(path)
                return
                
            for v in graph[u]:
                new_path = path + [v]
                dfs(v, new_path)
        dfs(0, [0])
        return ans
