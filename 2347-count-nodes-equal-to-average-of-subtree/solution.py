# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        ans = 0

        def traverse(root):
            nonlocal ans
            if not root:
                return 0, 0
            left_sum, left_st_node_count = traverse(root.left)
            right_sum, right_st_node_count = traverse(root.right)
            node_count = left_st_node_count + right_st_node_count + 1
            total_sum = left_sum + right_sum + root.val
            ans += total_sum // node_count == root.val
            return (
                total_sum,
                node_count,
            )

        traverse(root)
        return ans

