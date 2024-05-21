class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]: 
            return True
            
        def can_b_valid_palin(i, j, deleted):
            if deleted > 1:
                return False

            if i > j:
                return True

            if s[i] != s[j]:
                return can_b_valid_palin(i+1, j, deleted+1) or can_b_valid_palin(i, j-1, deleted+1)
            
            return  can_b_valid_palin(i+1, j-1, deleted)

        return can_b_valid_palin(0, len(s)-1, 0)
