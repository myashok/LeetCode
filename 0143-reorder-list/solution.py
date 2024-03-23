class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # Helper function to reverse a linked list
        def reverse_list(node):
            prev = None
            while node:
                temp = node.next
                node.next = prev
                prev = node
                node = temp
            return prev

        # Helper function to split the linked list into two halves
        def split_list(node):
            slow = fast = node
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            second_half = slow.next
            slow.next = None
            return node, second_half

        # Helper function to merge two linked lists
        def merge_lists(first, second):
            while first and second:
                temp1 = first.next
                temp2 = second.next
                first.next = second
                second.next = temp1
                first = temp1
                second = temp2

        if not head or not head.next:
            return

        first_half, second_half = split_list(head)
        second_half = reverse_list(second_half)
        merge_lists(first_half, second_half)

