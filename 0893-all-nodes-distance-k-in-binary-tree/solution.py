# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# distance - from root x
# distance - from root target y

# distance - of parent root p

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        parent = {}
        def traverse(node, p):
            if not node:
                return
            parent[node] = p
            traverse(node.right, node)
            traverse(node.left, node)
        
        visited = set()
        ans = []
        def dfs(node, level):
            if not node or node in visited:
                return
            visited.add(node)
            if level == k:
                ans.append(node.val)
                return
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
            dfs(parent[node], level + 1)
            
        traverse(root, None)
        dfs(target, 0)
        return ans


            
        
