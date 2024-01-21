class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        n = len(s)
        count = Counter(s)
        visited = set()
        ans = []
        for c in s:
            count[c] -= 1
            if c not in visited:
                while ans and ans[-1] > c and count[ans[-1]] > 0:
                    visited.remove(ans.pop())
                visited.add(c)
                ans.append(c)
        
        return ''.join(ans)        


