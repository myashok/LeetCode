class Solution:
    def findAnagrams(self, s2: str, s1: str) -> List[int]:
        s1_len = len(s1)
        s2_len = len(s2)
        
        if s2_len < s1_len:
            return []
        
        c1 = Counter(s1)
        c2 = Counter(s2[:s1_len])
        ans = []
        if sum((c1-c2).values()) == 0:
            ans.append(0)
        
        for i in range(s1_len, s2_len):
            c2[s2[i-s1_len]] -= 1
            c2[s2[i]] += 1
            if sum((c1-c2).values()) == 0:
                ans.append(i-s1_len+1)
        
        return ans
