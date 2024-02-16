class Solution:
    class UF:
        def __init__(self, n):
            self.parent = [i for i in range(n)]
            self.rank = [1]*n

        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
        
        def union(self, x, y, friends_size):
            rank = self.rank
            parent = self.parent
            root_x = self.find(x)
            root_y = self.find(y)

            if root_x == root_y:
                return False
            
            if rank[root_x] > rank[root_y]:
                rank[root_x] += rank[root_y]
                parent[root_y] = parent[root_x]
            else:
                rank[root_y] += rank[root_x]
                parent[root_x] = parent[root_y]
            
            return rank[root_x] == friends_size or rank[root_y] == friends_size
            
                

            
    
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort()
        uf = self.UF(n)
        for log in logs:
            time, u, v = log
            if uf.union(u, v, n):
                return time
        return -1
