class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)
        
        if s2_len < s1_len:
            return False
        
        c1 = Counter(s1)
        c2 = Counter(s2[:s1_len])
        
        if sum((c1-c2).values()) == 0:
            return True
        
        for i in range(s1_len, s2_len):
            c2[s2[i-s1_len]] -= 1
            c2[s2[i]] += 1
            if sum((c1-c2).values()) == 0:
                return True
        
        return False


        
