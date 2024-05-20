# Objective is to find valid string with least number of changes.
# If we use BFS and traverse levels, where levels represent number of changes/removals in the string then we will be able to find the valid strings corresponding to each level.
#Eg.
# starting = "()())()"
# Level 0 -> no valid string
# Level 1 -> "()()()", "(())()"
# Level 2 -> no valid string
# Level 3 -> "()()", "(())"
# In our case we want to minimize the change, so we will stop traversing into additional levels whenever we encounter a valid string in a level. In the above example we encounter valid string in Level 1, so we can stop traversing any further and just explore that same level to find out more valid strings.

class Solution:
    # To identify if the char is a parenthesis
    def isParenthesis(self, c):
        if c in set(["(", ")"]):
            return True
        return False
    
    # To check if the string is valid or not. Matching parenthesis
    def isValid(self, candidate):
            counter = 0
            for char in candidate:
                if char == "(": counter += 1
                elif char == ")": counter -= 1
                if counter < 0: return False
            # balanced?
            return counter == 0
     
                
    
    
    def removeInvalidParentheses(self, s: str) -> List[str]:
        queue = [s]
        seen = set()
        
        result = []
        dont_traverse = False
        while(queue):
            str = queue.pop(0)
            if str not in seen:
                seen.add(str)
            else:
                continue
            # Find if it is a valid string
            if self.isValid(str):
                # Add this to result and set the flag to stop traversing any further vertically.
                result.append(str)
                dont_traverse = True
            
            
            if not dont_traverse: 
                for i,p in enumerate(str):
                    if self.isParenthesis(p):
                        temp_str = str[0:i] + str[i+1:]
                        queue.append(temp_str)
        
            
        return result        
