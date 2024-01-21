class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k >= len(num):
            return "0"
        st = []
        for c in num:
            while st and k and st[-1] > c:
                st.pop()
                k -= 1            
            st.append(c)

        if k:
            st = st[:-k]
        
        return ''.join(st).lstrip("0") or "0"
