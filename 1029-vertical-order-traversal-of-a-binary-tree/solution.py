# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = defaultdict(list)
        def traverse(root, col, row):
            if not root:
                return
            ans[col].append((row, root.val))
            traverse(root.left, col - 1, row + 1)
            traverse(root.right, col + 1, row + 1)
        traverse(root, 0, 0)
        res = []
        for key in sorted(ans):
            res.append([val for _, val in sorted(ans[key])])
        return res

