class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st = list()
        for c in num:
            while st and k and st[-1] > c:
                st.pop()
                k -= 1
            
            if st or c is not '0':
                st.append(c)
        if k:
            st = st[:-k]
        return ''.join(st) or '0'
        
