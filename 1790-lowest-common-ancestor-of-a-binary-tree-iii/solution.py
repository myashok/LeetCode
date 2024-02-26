"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        visited = set()
        while p != None:
            visited.add(p.val)
            p = p.parent

        while q != None:
            if q.val in visited:
                return q
            q = q.parent
       
        return None
