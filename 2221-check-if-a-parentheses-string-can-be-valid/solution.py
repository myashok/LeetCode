class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 != 0:
            return False
        open_paren = []
        unlocked = []

        for i, c in enumerate(s):
            if locked[i] == "1":
                if c == "(":
                    open_paren.append(i)
                else:
                    if open_paren:
                        open_paren.pop()
                    elif unlocked:
                        unlocked.pop()
                    else:
                        return False
            else:
                unlocked.append(i)
        
        while open_paren:
            if not unlocked:
                return False
            
            open_idx = open_paren.pop()
            unlocked_idx = unlocked.pop()

            if unlocked_idx < open_idx:
                return False
        
        return True
