class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
      ans = [] 
      def inner(i, s: str):
        if i == len(s):
          ans.append(s)
          return
          
        ch = s[i]
        inner(i+1, s)

        if ch.isalpha():
          s = s[:i] + ch.swapcase() + s[i+1:]
          inner(i+1, s)

      inner(0, s)
      return ans


