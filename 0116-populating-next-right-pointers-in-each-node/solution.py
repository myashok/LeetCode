"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        q = deque()
        visited = set()
        q.append(root)
        visited.add(root)
        while q:
            q_size = len(q)
            prev_node = None
            for _ in range(q_size):
                node = q.popleft()
                if node.right:
                    q.append(node.right)
                    visited.add(node.right)
                if node.left:
                    q.append(node.left)
                    visited.add(node.left)
                node.next = prev_node
                prev_node = node
        return root
            

