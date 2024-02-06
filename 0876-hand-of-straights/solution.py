from sortedcontainers import SortedDict
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False
        c = Counter(hand)
        min_heap = list(c.keys())
        heapq.heapify(min_heap)
        while min_heap:
            smallest = min_heap[0]
            for i in range(smallest, smallest+groupSize):
                if c[i] == 0:
                    return False

                if c[i] == 1:
                    if i != min_heap[0]:
                        return False
                    heapq.heappop(min_heap)
                c[i] -= 1
        return True

       

