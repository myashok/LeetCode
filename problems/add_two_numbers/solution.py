# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        return self.helper(l1,l2,False)

    def helper(self,l1, l2,hasCarry):

        if l1 is None and l2 is None:
            return ListNode(1,None) if hasCarry else None

        if l1 is not None and l2 is not None:

            digit = l1.val + l2.val + 1 if hasCarry else l1.val + l2.val

            if digit >= 10:
                lastDigit = int(str(digit)[len(str(digit)) - 1])
                return ListNode(lastDigit, self.helper(l1.next, l2.next, True))
            else:
                return ListNode(digit, self.helper(l1.next, l2.next, False))

        elif l1 is not None and l2 is None:

            digit = l1.val + 1 if hasCarry else l1.val

            if digit >= 10:
                lastDigit = int(str(digit)[len(str(digit)) - 1])
                return ListNode(lastDigit, self.helper(l1.next, l2, True))
            else:
                return ListNode(digit, self.helper(l1.next, l2, False))

        elif l1 is None and l2 is not None:
            digit = l2.val + 1 if hasCarry else l2.val

            if digit >= 10:
                lastDigit = int(str(digit)[len(str(digit)) - 1])
                return ListNode(lastDigit, self.helper(l1, l2.next, True))
            else:
                return ListNode(digit, self.helper(l1, l2.next, False))

        return None