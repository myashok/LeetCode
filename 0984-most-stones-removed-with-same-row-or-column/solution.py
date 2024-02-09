class Solution:
    class UnionFind:
        def __init__(self):
            self.parent = {}
            self.rank = defaultdict(int)

        def find(self, x):
            if x not in self.parent:
                self.parent[x] = x
                
            if x != self.parent[x]:
                self.parent[x] = self.find(self.parent[x])
            
            return self.parent[x]

        def union(self, x, y):
            root_x, root_y = self.find(x), self.find(y)
            
            if root_x == root_y:
                return 
            
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
                self.rank[root_y] += 1
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

        def get_disjoint_sets_count(self):
            return sum(1 for k, v in self.parent.items() if k == v)


    def removeStones(self, stones):
        uf = self.UnionFind()
        for x, y in stones:
            uf.union(x, ~y)
        return len(stones) - uf.get_disjoint_sets_count()

