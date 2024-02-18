# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        min_val = -1 * 2 ** 31 - 1
        max_val = 2 ** 31 + 1
        def isValid(root):
            if not root:
                return True, min_val, max_val
            
            is_valid_left, lmx, lmn = isValid(root.left)
            is_valid_right, rmx, rmn = isValid(root.right)
            new_mx = max(lmx, rmx, root.val)
            new_mn = min(lmn, rmn, root.val)
            return ((lmx < root.val < rmn and is_valid_left and is_valid_right), new_mx, new_mn)
        
        return isValid(root)[0]
