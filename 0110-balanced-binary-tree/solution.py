# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(root):
            if not root:
                return True, -1

            left_is_balanced, left_height = check(root.left)
            right_is_balanced, right_height = check(root.right)
            return left_is_balanced and right_is_balanced and abs(left_height - right_height) <= 1, max(left_height, right_height) + 1
        
        return check(root)[0]
