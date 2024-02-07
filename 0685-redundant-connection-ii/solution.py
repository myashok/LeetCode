class Solution:
    class UF:
        def __init__(self, n):
            self.parent = [-1] * (n + 1)
            self.rank = [0] * (n + 1)

        def find(self, x):
            while self.parent[x] != -1:
                x = self.parent[x]
            return x
        
        def union(self, x, y):
            root_x = self.find(x)
            root_y = self.find(y)
            
            if root_x == root_y:
                return False  # Already in the same set
            
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

            return True

    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = self.UF(n)
        parent_dict = defaultdict(list)
        double_parent_node = old_parent = new_parent = -1
        for edge in edges:
            u, v = edge
            parent_dict[v].append(u)
            if len(parent_dict[v]) == 2:
                double_parent_node = v
                old_parent = parent_dict[v][0]
                new_parent = parent_dict[v][1]
                break

        if double_parent_node == -1:
            for edge in edges:
                if not uf.union(*edge):
                    return edge
        
        # double parent case is there
        for edge in edges:
            if edge != [new_parent, double_parent_node]:
                if not uf.union(*edge):
                    return [old_parent, double_parent_node]
        
        return [new_parent, double_parent_node]
            

                
