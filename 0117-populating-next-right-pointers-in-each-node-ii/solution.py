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
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        q = deque([root])
        while q:
            prevNode = None
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                node.next = prevNode
                prevNode = node
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
        return root
        
