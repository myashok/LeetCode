"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node = head
        list_to_copy = {None: None}
        while node:
            list_to_copy[node] = Node(node.val)
            node = node.next
        
        node = head
        while node:
            copy_node = list_to_copy[node]
            copy_node.next = list_to_copy[node.next]
            copy_node.random = list_to_copy[node.random]
            node = node.next
        return list_to_copy[head]
        
