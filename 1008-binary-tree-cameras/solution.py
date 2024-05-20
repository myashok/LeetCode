class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        covered = 1
        notCovered = 0
        hasCamera = 2

        self.cams = 0
        node = root
        def dfs(node):
            if not node: return covered
            # if not node.left and not node.right: return notCovered

            left = dfs(node.left)
            right = dfs(node.right)
            
            if left is notCovered or right is notCovered:
                self.cams += 1
                return hasCamera
            elif left is hasCamera or right is hasCamera:
                return covered
            else:
                return notCovered

        return self.cams + 1 if (dfs(node) is notCovered) else self.cams
