class Solution:
    def numberToWords(self, num: int) -> str:
        denomination = ["Hundred ", "Thousand ", "Million ", "Billion "]
        tens_name = ["","", "Twenty ", "Thirty ", "Forty ", "Fifty ", "Sixty ", "Seventy ", "Eighty ", "Ninety "]
        counting = ["", "One ", "Two ", "Three ", "Four ", "Five ", "Six ", "Seven ", "Eight ", "Nine ", "Ten ", "Eleven ", "Twelve ", "Thirteen ", "Fourteen " , "Fifteen ", "Sixteen ", "Seventeen ", "Eighteen ", "Nineteen ",]
        level = 0
        def number(n, level):
            ans = []
            if n >= 100:
                r_n = n%100
                n = n//100
                ans.append(counting[n])
                ans.append(denomination[0])
                n = r_n
            if n > 19:
                ans.append(tens_name[n//10])
                ans.append(counting[n%10])
            else:
                ans.append(counting[n])
            
            ans = [i for i in ans if i]

            if level >= 1 and ans:
                ans.append(denomination[level])
            return ans

        res = []       
        while num > 0:
            curr_denomination = num % 1000
            num //= 1000
            res = number(curr_denomination, level) + res
            level += 1
        return "Zero" if not res else "".join(res)[:-1]
