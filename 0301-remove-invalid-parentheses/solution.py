from collections import deque
from typing import List

class Solution:
    def isParenthesis(self, c):
        return c in {"(", ")"}
    
    def isValid(self, candidate):
        counter = 0
        for char in candidate:
            if char == "(": counter += 1
            elif char == ")": counter -= 1
            if counter < 0: return False
        return counter == 0
    
    def removeInvalidParentheses(self, s: str) -> List[str]:
        queue = deque([s])
        seen = set([s])
        result = []
        found = False

        while queue:
            current = queue.popleft()
            
            if self.isValid(current):
                result.append(current)
                found = True
            
            if found:
                continue
            
            for i in range(len(current)):
                if self.isParenthesis(current[i]):
                    temp_str = current[:i] + current[i+1:]
                    if temp_str not in seen:
                        queue.append(temp_str)
                        seen.add(temp_str)
        
        return result if result else [""]

