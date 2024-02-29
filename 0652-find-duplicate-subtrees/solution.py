from collections import defaultdict

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def traverse(root):
            if not root:
                return ""
            
            left_structure = traverse(root.left)
            right_structure = traverse(root.right)
            
            structure = f'{left_structure},{right_structure},{root.val}'
            subtree_hash[structure].append(root)
            
            return structure
        
        subtree_hash = defaultdict(list)
        traverse(root)
        
        return [nodes[0] for nodes in subtree_hash.values() if len(nodes) > 1]

