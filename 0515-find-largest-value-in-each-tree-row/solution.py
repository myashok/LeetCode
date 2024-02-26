# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        row_max = defaultdict(lambda : -math.inf)
        def dfs(root, row_no):
            if not root:
                return
            row_max[row_no] = max(row_max[row_no], root.val)
            dfs(root.left, row_no + 1)
            dfs(root.right, row_no + 1)
        dfs(root, 0)
        return row_max.values()
