class TopVotedCandidate:
    def _build_time_aware_winner(self, persons, times):
        time_aware_winner = {}
        winner = persons[0]
        time_aware_winner[times[0]] = winner
        freq = defaultdict(int)
        freq[persons[0]] = 1  
        for i, person in enumerate(persons[1:]):
            freq[person] += 1
            winner = person if freq[person] >= freq[winner] else winner
            time_aware_winner[times[i+1]] = winner

        return time_aware_winner

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.time_aware_winner = self._build_time_aware_winner(persons, times)
        print(self.time_aware_winner)

    def q(self, t: int) -> int:
        if t in self.time_aware_winner:
            return self.time_aware_winner[t]
        else:
            index = bisect.bisect(self.times, t)
            return self.time_aware_winner[self.times[index-1]]
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
