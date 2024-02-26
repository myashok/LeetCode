# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def get_max_path(root):
            if not root:
                return -math.inf, 0
            left_max, lmax_gain = get_max_path(root.left)
            right_max, rmax_gain = get_max_path(root.right)
            lmax_gain = max(0, lmax_gain)
            rmax_gain = max(0, rmax_gain)
            return max(
                left_max,
                right_max,
                lmax_gain + rmax_gain + root.val,
            ), (lmax_gain + root.val if lmax_gain > rmax_gain else rmax_gain + root.val)

        return get_max_path(root)[0]

