class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        graph = defaultdict(list)
        for v1, v2 in prerequisites:
            indegree[v1] += 1
            graph[v2].append(v1)

        q = deque([i for i in range(numCourses) if indegree[i] == 0])
        order = []
        while q:
            cur = q.popleft()
            order.append(cur)
            for nei in graph[cur]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        if len(order) < numCourses:
            return []
        return order
