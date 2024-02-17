class Solution:

    def majorityElement(self, nums):
        if not nums:
            return [] 

        ct1, ct2, c1, c2 = 0, 0, None, None
        for n in nums:
            if c1 == n:
                ct1 += 1
            elif c2 == n:
                ct2 += 1
            elif ct1 == 0:
                c1 = n
                ct1 += 1
            elif ct2 == 0:
                c2 = n
                ct2 += 1
            else:
                ct1 -= 1
                ct2 -= 1

        result = []
        if nums.count(c1) > len(nums)//3:
            result.append(c1)
        if nums.count(c2) > len(nums)//3:
            result.append(c2)

        return result
