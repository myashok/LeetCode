class Solution:
    def findNthDigit(self, n: int) -> int:
        # 9 1 digit number
        # 90 2 digit number
        # 900 3 digit number

        digits_per_number = 1
        number_count = 9
        while digits_per_number * number_count < n:
            n -= digits_per_number * number_count
            digits_per_number += 1
            number_count *= 10

        number = 10 ** (digits_per_number - 1) + (n - 1) // digits_per_number
        return int(str(number)[(n - 1) % digits_per_number])
