# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def traverse(root):
            if not root:
                return ["#"]
            ans = []
            ans.append(str(root.val))
            ans.extend(traverse(root.left))
            ans.extend(traverse(root.right))
            return ans
            
        ans = traverse(root)
        return ",".join(ans)
            
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(",")[:-1]
        def traverse(data, index):
            if index >= len(data):
                return None, index
            if data[index] == '#':
                return None, index
            root = TreeNode(int(data[index]))
            root.left, index = traverse(data, index+1)
            root.right, index = traverse(data, index+1)
            return root, index
        return traverse(data, 0)[0]
            
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
