# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def traverse(root, mx):
            if not root:
                return 0
            
            new_max = max(mx, root.val)
            return (
                traverse(root.left, new_max)
                + traverse(root.right, new_max)
                +  (1 if root.val > mx - 1 else 0)
            )

        return traverse(root, -(10**5))

