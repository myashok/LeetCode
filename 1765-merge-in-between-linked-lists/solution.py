# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        second_list_start = list2
        node = list2
        while node.next:
            node = node.next
        second_list_end = node
        i = 1
        node = list1
        while i < a:
            node = node.next
            i += 1
        temp = node.next
        node.next = second_list_start
        while i <= b:
            temp = temp.next
            i += 1
        second_list_end.next = temp
        return list1
