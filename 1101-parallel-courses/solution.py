from collections import defaultdict, deque
from typing import List

class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        g = defaultdict(list)
        in_degree = [0] * (n + 1)
        for rel in relations:
            u, v = rel
            g[u].append(v)
            in_degree[v] += 1
        
        def bfs():
            queue = deque([i for i in range(1, n + 1) if in_degree[i] == 0])
            semester = course_taken = 0
            while queue:
                semester += 1
                for _ in range(len(queue)):
                    u = queue.popleft()
                    course_taken += 1
                    for v in g[u]:
                        in_degree[v] -= 1
                        if in_degree[v] == 0:
                            queue.append(v)
            return semester if course_taken == n else -1
            
        return bfs()
