class Solution:
    def nextClosestTime(self, time: str) -> str:
        digits = sorted(set([time[0], time[1], time[3], time[4]]))
        ans = ""
        n = len(time)
        lsd = next(iter(digits))
        for i in range(len(time) - 1, -1, -1):
            if time[i] == ':':
                continue
            for digit in digits:
                if digit > time[i]:
                    lst_time = list(time)
                    lst_time[i] = digit
                    for i in range(i+1, n):
                        if lst_time[i] == ":":
                            continue
                        else:
                            lst_time[i] = lsd
                    temp_time = ''.join(lst_time)
                    hour, minute = temp_time.split(":")
                    if "00" <= hour <= "23" and "00" <= minute <= "59":
                        ans = temp_time
                        return ans
        
        return f"{lsd}{lsd}:{lsd}{lsd}" if not ans else ans


            


        
