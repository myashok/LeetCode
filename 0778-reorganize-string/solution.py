class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        # odd 
        if any([freq > (len(s) + 1) // 2 for _, freq in count.items()]):
            return ""
        ans = [0]*(len(s))
        count_list = list(sorted(count.items(), key=lambda x: -x[1]))
        if count_list[0][1] > (len(s) + 1) // 2:
            return ""
        i = 0
        for c, freq in count_list:
            for _ in range(freq):
                ans[i] = c
                i += 2
                if i >= len(s):
                    i = 1

        return "".join(ans)


            

