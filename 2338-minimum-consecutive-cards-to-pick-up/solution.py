class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        cards_last_seen = {}
        ans = math.inf
        for i in range(len(cards)):
            if cards[i] in cards_last_seen:
                ans = min(ans, i - cards_last_seen[cards[i]] + 1)
            cards_last_seen[cards[i]] = i
        return -1 if ans == math.inf else ans
