class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree = [0]*n
        for edge in edges:
            indegree[edge[1]] += 1
        return [i for i in range(n) if not indegree[i]]
