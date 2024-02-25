from collections import defaultdict
from typing import List

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # Initialize the set with the initial person who knows the secret
        secret_known_list = set([0, firstPerson])
        
        # Sort meetings based on time
        meetings.sort(key=lambda x: x[2])
        
        # Initialize variables
        prev_meet_time = -1
        g = defaultdict(list)  # Graph to store connections between people
        
        # Depth-first search function to propagate the secret
        def dfs(g, u):
            secret_known_list.add(u)
            for v in g[u]:
                if v not in secret_known_list:
                    dfs(g, v)
        
        # Iterate through meetings
        for p1, p2, time in meetings:
            # If the time is different from the previous meeting
            if time != prev_meet_time:
                # Perform DFS on the graph to propagate the secret
                for u in g:
                    if u in secret_known_list:
                        dfs(g, u)
                
                # Reset the graph for the current time
                g = defaultdict(list)
                g[p1].append(p2)
                g[p2].append(p1)
            else:
                # Add connections for the current time
                g[p1].append(p2)
                g[p2].append(p1)
            
            # Update the previous meeting time
            prev_meet_time = time
        
        # Perform DFS for the last time instance
        for u in g:
            if u in secret_known_list:
                dfs(g, u)
        
        return secret_known_list

