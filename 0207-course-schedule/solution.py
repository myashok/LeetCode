class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = defaultdict(list)
        for a, b in prerequisites:
            g[b].append(a)
        
        visited = set()
        def cycle(u, recursion_stack):
            visited.add(u)
            recursion_stack.append(u)
            for v in g[u]:
                if v in recursion_stack:
                    return True
                if v not in visited:
                    if cycle(v, recursion_stack):
                        return True

            recursion_stack.pop()
            return False



        for i in range(numCourses):
            if i not in visited:
                if cycle(i, []):
                    return False
        return True

