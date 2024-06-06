class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [['$', 0]]
        for c in s:
            if stack[-1][0] == c:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([c, 1])
        
        result = []
        for char, count in stack:
            result.append(char * count)
        
        return ''.join(result)
