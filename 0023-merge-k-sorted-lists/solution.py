import heapq

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode

        Note: this is Python2 code
        """

        # Create a dummy head and a pointer
        head = point = ListNode(0)
        
        # Create a min-heap
        heap = []
        setattr(ListNode, "__lt__", lambda self, other: self.val <= other.val)
        # Push the first element of each list into the heap
        for l in lists:
            if l:
                heapq.heappush(heap, (l.val, l))
        
        while heap:
            val, node = heapq.heappop(heap)
            point.next = node
            point = point.next
            node = node.next
            if node:
                heapq.heappush(heap, (node.val, node))
        
        return head.next

