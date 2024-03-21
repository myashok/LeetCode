# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node):
            nonlocal head
            if not node:
                return node

            if not node.next:
                head = node
                return head
                         
            reverse_list_start = reverse(node.next)
            node.next = None
            reverse_list_start.next = node
            return node   
        reverse(head)
        return head
