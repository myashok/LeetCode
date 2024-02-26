class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum & 1:
            return []
        num = 2
        curr_sum = 0
        ans = []
        while curr_sum + num <= finalSum:
            ans.append(num)
            curr_sum += num
            num += 2
        ans[-1] += finalSum - curr_sum 
        return ans
