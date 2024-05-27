# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxAncestorDiff(self, node: Optional[TreeNode], curr_min = 100000, curr_max = 0) -> int:
        if not node:
            return curr_max - curr_min

        curr_min = min(curr_min, node.val)
        curr_max = max(curr_max, node.val)
        
        # Recurse for left and right children
        left_diff = self.maxAncestorDiff(node.left, curr_min, curr_max)
        right_diff = self.maxAncestorDiff(node.right, curr_min, curr_max)
        
        # Return the maximum difference found in the subtree rooted at this node
        return max(left_diff, right_diff)

    
    

