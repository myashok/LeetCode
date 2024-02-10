class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # Enumerate tasks with their indices
        indexed_tasks = [(task[0], task[1], index) for index, task in enumerate(tasks)]
        # Sort tasks based on enqueue time, processing time, and index
        indexed_tasks.sort()

        # Priority queue to keep track of available tasks based on processing time and index
        available_tasks = []
        # Initialize current time and index
        time, index = 0, 0
        # Result list to store the order of processed tasks
        result = []

        while len(result) < len(tasks):
            # Add tasks that are available at the current time to the priority queue
            while index < len(indexed_tasks) and indexed_tasks[index][0] <= time:
                enqueue_time, processing_time, task_index = indexed_tasks[index]
                heapq.heappush(available_tasks, (processing_time, task_index))
                index += 1

            # If CPU is idle and available tasks exist, process the task with the shortest processing time
            if not available_tasks:
                time = indexed_tasks[index][0]
                continue

            # Dequeue the task with the shortest processing time
            processing_time, task_index = heapq.heappop(available_tasks)
            # Update current time
            time += processing_time
            # Append the index of the processed task to the result
            result.append(task_index)

        return result
