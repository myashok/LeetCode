# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = 1
        curr = root
        while curr.left:
            curr = curr.left
            left += 1
        
        right = 1
        curr = root
        while curr.right:
            curr = curr.right
            right += 1
        
        if left == right:
            return (1 << left) - 1

        return self.countNodes(root.left) + self.countNodes(root.right) + 1
        
