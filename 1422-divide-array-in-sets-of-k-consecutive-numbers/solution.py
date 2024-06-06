class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False

        count = Counter(nums)
        for num in nums:
            start = num
            if not count[start]:
                continue
            while count[start-1]:
                start -= 1
            while start <= num:
                while count[start]:
                    for i in range(start, start + k):
                        if count[i] == 0:
                            return False
                        count[i] -= 1
                start += 1
        return True

