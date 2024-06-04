class Solution:
    def customSortString(self, order: str, s: str) -> str:
        key = {order[i]:i + 1 for i in range(len(order))}
        return "".join(sorted(s, key= lambda c: key[c] if c in key else 0))
