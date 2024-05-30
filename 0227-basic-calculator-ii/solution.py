class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        current_num = 0
        operator = '+'  # Current operator starts with '+'
        idx = 0

        while idx < len(s):
            char = s[idx]

            if char.isdigit():
                current_num = current_num * 10 + int(char)
            
            if char in '+-*/' or idx == len(s) - 1:
                if operator == '+':
                    stack.append(current_num)
                elif operator == '-':
                    stack.append(-current_num)
                elif operator == '*':
                    stack[-1] = stack[-1] * current_num
                elif operator == '/':
                    stack[-1] = int(stack[-1] / current_num)  # Integer division

                operator = char
                current_num = 0

            idx += 1

        return sum(stack)

