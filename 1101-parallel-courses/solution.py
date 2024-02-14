class Solution:
    def minimumSemesters(self, N: int, relations: List[List[int]]) -> int:
        graph = {i: [] for i in range(1, N + 1)}
        for start_node, end_node in relations:
            graph[start_node].append(end_node)

        # check if the graph contains a cycle
        visited = {}
        def dfs_max_path(node: int) -> int:
            # return the longest path (inclusive)
            if node in visited:
                return visited[node]
            
            visited[node] = -1
            max_length = 1
            for end_node in graph[node]:
                length = dfs_max_path(end_node)
                if length == -1:
                    return -1
                max_length = max(length+1, max_length)
            
            # store it
            visited[node] = max_length
            return max_length
        
        ans = 0
        for node in graph.keys():
            length = dfs_max_path(node)
            if length == -1:
                return -1
            else:
                ans = max(ans, length)
        return ans
