class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d={0:1}
        c,l=0,0
        
        for i in range(len(nums)):
            c=c+nums[i]
            m=c%k
            if m in d:
                l=l+d[m]
                d[m]+=1
            else:
                d[m]=1
        return l


