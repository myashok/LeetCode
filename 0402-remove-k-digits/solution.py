class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)

        # Remove digits from the end if k is still positive
        while k > 0 and stack:
            stack.pop()
            k -= 1

        # Remove leading zeros
        while stack and stack[0] == '0':
            stack.pop(0)

        # If stack is empty, return "0"
        if not stack:
            return "0"

        # Join digits in the stack and return the resulting string
        return ''.join(stack)

        
    
        
