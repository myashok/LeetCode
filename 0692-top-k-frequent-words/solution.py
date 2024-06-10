class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = collections.Counter(words)
        heap = [(-count, word) for word, count in counts.items()]
        heapq.heapify(heap) 
        return [heapq.heappop(heap)[1] for _ in range(k)]
