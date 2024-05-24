class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # Initialize pointers for num1 and num2, and the carry
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        result = []
        
        # Loop through both strings from the end to the beginning
        while i >= 0 or j >= 0 or carry:
            # Get the current digits, or 0 if the index is out of bounds
            x1 = int(num1[i]) if i >= 0 else 0
            x2 = int(num2[j]) if j >= 0 else 0
            
            # Calculate the sum and carry
            total = x1 + x2 + carry
            carry = total // 10
            result.append(total % 10)
            
            # Move to the next digits
            i -= 1
            j -= 1
        
        # Since we added digits in reverse order, reverse the result
        return ''.join(map(str, result[::-1]))

