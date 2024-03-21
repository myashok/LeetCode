class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        count_values = sorted(count.values())
        gaps = count_values[-1] - 1
        free_slots = gaps * n
        for freq in count_values[:-1]:
            free_slots -= min(gaps, freq)
        return len(tasks) + (0 if free_slots < 0 else free_slots)
