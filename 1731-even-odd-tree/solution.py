# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        even = 0
        odd = 1
        dq = deque()
        dq.append((root, even))
        while dq:
            size = len(dq)
            prev_node_val = -1
            for i in range(size):
                node, parity = dq.popleft()
                if parity == even:
                    if not (node.val & 1 and (node.val > prev_node_val or prev_node_val == -1)):
                        return False
                elif parity == odd:
                    if not ((not node.val & 1) and (node.val < prev_node_val or prev_node_val == -1)):
                        return False
                if node.left:
                    dq.append((node.left, not parity))
                if node.right:
                    dq.append((node.right, not parity))
                prev_node_val = node.val

        return True
                    

