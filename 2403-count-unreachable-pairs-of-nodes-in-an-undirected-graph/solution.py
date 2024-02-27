from collections import defaultdict
from typing import List

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        # Initialize variables to keep track of counts
        previous_visited_count = ans = 0
        visited = set()  # Keep track of visited nodes
        g = defaultdict(list)  # Graph representation using adjacency list
        
        # Construct the graph
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        
        # Depth First Search (DFS) function to traverse the graph
        def dfs(u):
            visited.add(u)
            for v in g[u]:
                if v not in visited:
                    dfs(v)

        # Iterate through all nodes in the graph
        for i in range(n):
            if i not in visited:  # If the node has not been visited yet
                dfs(i)  # Perform DFS from this node
                # Calculate the number of pairs formed by nodes in the current island and previously visited islands
                curr_visited_count = len(visited)
                curr_island_len = curr_visited_count - previous_visited_count
                ans +=  curr_island_len * previous_visited_count
                previous_visited_count = curr_visited_count  # Update the count of visited nodes
                        
        return ans

