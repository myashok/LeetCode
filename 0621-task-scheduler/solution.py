class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_freq = Counter(tasks)
        max_heap = [-freq for freq in task_freq.values()]
        heapq.heapify(max_heap)
        cooling_queue = deque()
        time = 0
        while max_heap or cooling_queue:
            time += 1
            if max_heap:
                most_freq_task = -heapq.heappop(max_heap)
                if most_freq_task - 1 > 0:
                    cooling_queue.append((most_freq_task - 1, time + n))
            if cooling_queue and cooling_queue[0][1] == time:
                heapq.heappush(max_heap, -cooling_queue.popleft()[0])
        return time

        
