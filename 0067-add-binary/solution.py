class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        i = len(a) - 1
        j = len(b) - 1
        ans = []
        while i >= 0 or j >= 0 or carry:
            ai_int = int(a[i]) if i >= 0 else 0
            bj_int = int(b[j]) if j >= 0 else 0
            curr_digit = (ai_int+ bj_int + carry)%2
            carry = (ai_int + bj_int + carry)//2
            ans.append(str(curr_digit))
            i -= 1
            j -= 1
        return "".join(ans)[::-1]
