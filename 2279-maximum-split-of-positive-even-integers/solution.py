class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum & 1:
            return []
        first_num = curr_sum = 2
        ans = []
        ans.append(first_num)
        while curr_sum < finalSum:
            first_num += 2
            if curr_sum + first_num <= finalSum:
                ans.append(first_num)
                curr_sum += first_num
            else:
                ans[-1] += (finalSum - curr_sum)
                break
        return ans
