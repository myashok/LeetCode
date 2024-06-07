# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def solve(node):
            if not node:
                return None, None
            lhead, ltail = solve(node.left)
            rhead, rtail = solve(node.right)
            
            if lhead:
                node.right = lhead
                node.left = None  # Ensure left child is set to None
                ltail.right = rhead
            else:
                node.right = rhead
            
            tail = (rtail if rtail else ltail) or node
            return node, tail
        
        solve(root)

