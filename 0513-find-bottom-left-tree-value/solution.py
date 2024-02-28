# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        def solve(root, depth):
            if not root:
                return -math.inf, depth
            left_value, ldepth = solve(root.left, depth + 1)
            right_value, rdepth = solve(root.right, depth + 1)
            if ldepth >= rdepth and left_value != -math.inf:
                res = left_value, ldepth
            elif ldepth < rdepth or right_value != -math.inf:
                res = right_value, rdepth
            else:
                res = root.val, depth
            return res

        return solve(root, 1)[0]

