class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            nonlocal moves
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            moves += abs(left) + abs(right)
            return node.val + left + right - 1
        
        moves = 0
        dfs(root)
        return moves

