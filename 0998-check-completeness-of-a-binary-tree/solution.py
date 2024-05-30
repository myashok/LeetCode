# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        q = deque([root])
        missing_encounterd = False
        while q:
            node = q.popleft()
            if node.right and not node.left:
                return False
            if not node.right and not missing_encounterd:
                missing_encounterd = True
            elif missing_encounterd and (node.left or node.right):
                return False
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return True
            



    
