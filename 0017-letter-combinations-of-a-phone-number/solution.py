class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter_dict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []
        def solve(i, str_arr):
            if i == len(digits) and str_arr:
                res.append(''.join(str_arr))
                return
            
            for c in letter_dict[digits[i]]:
                str_arr.append(c)
                solve(i+1, str_arr)
                str_arr.pop()
        digits and solve(0, [])
        return res

