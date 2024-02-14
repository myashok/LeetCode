# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def traverse(root, mx, mn, parent):
            if not root:
                return 0
            node_max = 0
            if parent != None:
               node_max = max(abs(mx - root.val), abs(mn - root.val))  
            left_max = traverse(root.left, max(mx, root.val), min(mn, root.val), root)
            right_max = traverse(root.right, max(mx, root.val), min(mn, root.val), root)
            return max(node_max, left_max, right_max)
        return traverse(root, 0, 10**5+1, None)
