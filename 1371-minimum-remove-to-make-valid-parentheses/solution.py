class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        st = []
        flags = [False] * len(s)
        
        for i, c in enumerate(s):
            if c == '(':
                st.append(i)
            elif c == ')':
                if st:
                    st.pop()
                else:
                    flags[i] = True
        
        for i in st:
            flags[i] = True
        
        return ''.join(c for i, c in enumerate(s) if not flags[i])

