class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        passengers = sorted(passengers)
        cur = 0
        for time in sorted(buses):
            cap = capacity
            while cur < len(passengers) and passengers[cur] <= time and cap > 0:
                cur += 1
                cap -= 1

        best = time if cap > 0 else passengers[cur - 1]
        while cur > 0 :
            if best != passengers[cur-1]:
                return best
            best -= 1
            cur -= 1

        return best
