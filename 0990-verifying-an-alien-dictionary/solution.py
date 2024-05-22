#
# @lc app=leetcode id=953 lang=python3
#
# [953] Verifying an Alien Dictionary
#
from typing import List
# @lc code=start
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        rank = {}
        for i, c in enumerate(order):
            rank[c] = i
        
        for i in range(len(words) - 1):
            j = i + 1
            w1 = w2 = 0
            while w1 < len(words[i]) and w2 < len(words[j]):
                if words[i][w1] != words[j][w2] and rank[words[i][w1]] > rank[words[j][w2]]:
                    return False
                elif words[i][w1] != words[j][w2]:
                    break
                w1 += 1
                w2 += 1
            if (w1 == len(words[i])  or w2 == len(words[j])) and len(words[i]) > len(words[j]):
                return False
        return True

        
# @lc code=end


