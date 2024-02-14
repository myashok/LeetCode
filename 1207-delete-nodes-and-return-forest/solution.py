# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        ans = []
        def postorder(root, parent):
            if not root:
                return
            postorder(root.left, root)
            postorder(root.right, root)
            if root.val in to_delete:
                if parent == None:
                    if root.left:
                        ans.append(root.left)
                    if root.right:
                        ans.append(root.right)
                else:
                    if root.left:
                        ans.append(root.left)
                    if root.right:
                        ans.append(root.right)
                    if parent.right and parent.right.val == root.val:
                        parent.right = None
                    if parent.left and parent.left.val == root.val:
                        parent.left = None
        
        postorder(root, None)
        if root and root.val not in to_delete:
            ans.append(root)

        return ans

