# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def solve(root):
            if not root:
                return 0, 0
            left_diameter, left_height = solve(root.left)
            right_diameter, right_height = solve(root.right)
            return max(left_diameter, right_diameter, left_height + right_height), 1 + max(left_height, right_height)
        return solve(root)[0]
