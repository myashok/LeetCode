# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @cache
        def solve(root, parent_taken):
            if not root:
                return 0
            if parent_taken:
                return solve(root.left, False) + solve(root.right, False)
            else:
                return max(solve(root.left, False) + solve(root.right, False), root.val + solve(root.left, True) + solve(root.right, True))

        return solve(root, False)
        
