class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i):
            visited.add(i)
            # Traverse all the nodes connected to this node
            for j in range(n):
                if isConnected[i][j] == 1 and j not in visited:
                    dfs(j)


        n = len(isConnected)
        visited = set()
        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        return count
