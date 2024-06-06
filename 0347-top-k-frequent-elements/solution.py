class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = []
        for key, value in freq.items():
            if len(heap) < k:
                heapq.heappush(heap, (value, key))
            elif value > heap[0][0]:
                heapq.heappushpop(heap, (value, key))
        
        ans = []
        while k > 0:
            k -= 1
            ans.append(heappop(heap)[1])
        
        return ans
