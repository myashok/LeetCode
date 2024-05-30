# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 1, 2, 3 4, 5, 6 , 7 , 8, 9, 10, 11
            #   6
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        list_array = []
        while head:
            list_array.append(head.val)
            head = head.next

        def constructTree(l, r):
            if l > r or l < 0 or r >= len(list_array):
                return None
            if l == r:
                return TreeNode(list_array[l])
            mid = (l+r) // 2
            left = constructTree(l, mid - 1)
            right = constructTree(mid + 1, r)
            return TreeNode(list_array[mid], left, right)
       
        return constructTree(0, len(list_array) - 1)
            

