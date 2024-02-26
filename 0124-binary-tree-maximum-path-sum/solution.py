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
                return -math.inf, -math.inf
            left_max, lheight_max = get_max_path(root.left)
            right_max, rheight_max = get_max_path(root.right)
            lh_max = 0
            rh_max = 0
            if lheight_max != -math.inf:
                lh_max = lheight_max
            if rheight_max != -math.inf:
                rh_max = rheight_max

            return max(left_max, right_max, lh_max + rh_max + root.val, root.val, lh_max + root.val, rh_max + root.val), (
                max(lh_max + root.val, root.val)
                if lheight_max > rheight_max
                else  max(rh_max + root.val, root.val)
            )

        return get_max_path(root)[0]

