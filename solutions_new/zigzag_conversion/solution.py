class Solution:
    def convert(self, s: str, num_rows: int) -> str:
        if num_rows == 1: return s
        rows = [""]* num_rows
        step  = 1
        curr_row = 0
        for char in s:
            rows[curr_row] += char
            if curr_row == 0:
                step = 1
            if curr_row == num_rows - 1:
                step = -1
            curr_row += step
        
        return "".join(rows)
