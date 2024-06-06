class Solution:
    def findItinerary(self, tickets):
        targets = collections.defaultdict(list)
        for a, b in tickets:
            targets[a].append(b)
        
        for key in targets:
            targets[key].sort(reverse=True)
            
        route = []
        def visit(airport):
            while targets[airport]:
                visit(targets[airport].pop())
            route.append(airport)
        visit('JFK')
        return route[::-1]
