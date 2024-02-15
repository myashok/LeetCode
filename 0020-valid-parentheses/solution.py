class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for c in s:
            if c in ('(', '{', '['):
                st.append(c)
            elif st and (st[-1] == '{' and c == '}'):
                st.pop()
            elif st and (st[-1] == '(' and c == ')'):
                st.pop()
            elif st and (st[-1] == '[' and c == ']'):
                st.pop()
            else:
                return False
        
        return len(st) == 0
