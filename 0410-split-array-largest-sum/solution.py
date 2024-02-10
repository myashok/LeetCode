class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def can_this_sum_possible(guess_sum):
            cnt = curr_sum = 0
            for num in nums:
                curr_sum += num
                if curr_sum > guess_sum:
                    curr_sum = num
                    cnt += 1

            return cnt < k
        
        h, l = sum(nums), max(nums)
        while l < h:
            guess_sum = (l + h)//2
            if can_this_sum_possible(guess_sum):
                h = guess_sum
            else:
                l = guess_sum + 1

        return l
