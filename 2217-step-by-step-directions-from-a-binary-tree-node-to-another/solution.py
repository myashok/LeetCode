# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def lca(root):
            if not root or root.val in (startValue, destValue):
                return root
            left_lca, right_lca = lca(root.left), lca(root.right)
            if left_lca and right_lca:
                return root
            return left_lca if left_lca else right_lca
        
        lca_node = lca(root)
        def traverse(root, p):
            if not root:
                return None
            if root.val == p:
                return "*"
            left_path =  traverse(root.left, p)
            right_path = traverse(root.right, p)
            if left_path:
                return "L" + left_path
            elif right_path:
                return "R" + right_path
            else:
                return None

        start_path = traverse(lca_node, startValue)
        dest_path = traverse(lca_node, destValue)

        return "U"*(len(start_path[:-1])) + dest_path[:-1]
