class Solution:


    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        ans = ""
        def lcs_dp(S, word):
            i = 0
            for c in S:
                if i < len(word) and word[i] == c:
                    i += 1
            return i == len(word)

        for word in dictionary:
            if len(ans) < len(word) and len(s) >= len(word):
                if lcs_dp(s, word):
                    ans = word
            elif len(ans) == len(word) and word < ans:
                if lcs_dp(s, word):
                    ans = word

        return ans
