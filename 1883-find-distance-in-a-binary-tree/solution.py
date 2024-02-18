# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        
        def distance(root, val, dist):
            if root is None:
                return -1

            if root.val == val:
                return dist

            left_dist = distance(root.left, val, dist + 1)
            if left_dist >= 0:
                return left_dist

            right_dist = distance(root.right, val, dist + 1)
            return right_dist

        def findLCA(root: Optional[TreeNode]) -> TreeNode:
            if not root:
                return None
            if root.val in (p, q):
                return root

            left_lca = findLCA(root.left)
            right_lca = findLCA(root.right)

            if left_lca and right_lca:
                return root
            
            return left_lca if left_lca else right_lca
        
        lca_node = findLCA(root)
        return distance(lca_node, p, 0) + distance(lca_node, q, 0)

