class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        col_index_map = defaultdict(lambda :defaultdict(list))
        def dfs(root, row, col):
            if not root:
                return
            dfs(root.left, row + 1, col - 1)
            dfs(root.right, row + 1, col + 1)
            col_index_map[col][row].append(root.val)
        dfs(root, 0, 0)
        ans = []
        for col_val in sorted(col_index_map):
            temp = []
            for row_val in sorted(col_index_map[col_val]):
                temp += col_index_map[col_val][row_val]
            ans.append(temp)
        return ans
