# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total_sum = 0
        
        def traverse(node, curr_sum):
            nonlocal total_sum
            if not node:
                return
                
            curr_sum = curr_sum * 10 + node.val
            
            if not node.left and not node.right:
                total_sum += curr_sum
                return

            traverse(node.left, curr_sum)
            traverse(node.right, curr_sum)
        
        traverse(root, 0)
        return total_sum

