class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        
        if not root:
            return []

        height = {}

        def set_heights(node):
            if not node:
                return -1
            node_height = max(set_heights(node.left), set_heights(node.right)) + 1
            height[node.val] = node_height
            return node_height

        set_heights(root)

        cache = {}

        def set_the_second_best_height_if_not_node(
            node, second_best_height_without_node, depth
        ):
            if not node:
                return

            cache[node.val] = second_best_height_without_node
            left_node_height = height[node.left.val] if node.left else -1
            right_node_height = height[node.right.val] if node.right else -1

            if left_node_height > right_node_height:
                second_best_height_without_node = max(
                    second_best_height_without_node, right_node_height + depth + 1
                )
                set_the_second_best_height_if_not_node(
                    node.left, second_best_height_without_node, depth + 1
                )

            else:
                second_best_height_without_node = max(
                    second_best_height_without_node, left_node_height + depth + 1
                )
                set_the_second_best_height_if_not_node(
                    node.right, second_best_height_without_node, depth + 1
                )

        set_the_second_best_height_if_not_node(root, -1, 0)

        # Process queries
        result = []
        for query in queries:
            if query not in cache:
                result.append(height[root.val])
            else:
                result.append(cache[query])

        return result

