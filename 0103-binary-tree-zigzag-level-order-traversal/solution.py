# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
    
        results = []
        current_level = deque([root])
        left_to_right = True
        
        while current_level:
            level_size = len(current_level)
            current_values = []
            
            for _ in range(level_size):
                if left_to_right:
                    node = current_level.popleft()
                    current_values.append(node.val)
                    if node.left:
                        current_level.append(node.left)
                    if node.right:
                        current_level.append(node.right)
                else:
                    node = current_level.pop()
                    current_values.append(node.val)
                    if node.right:
                        current_level.appendleft(node.right)
                    if node.left:
                        current_level.appendleft(node.left)
            
            results.append(current_values)
            left_to_right = not left_to_right
        
        return results
