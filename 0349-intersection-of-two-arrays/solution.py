class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        stt = [False] * 1001
        for i in nums1:
            stt[i] = True
        
        for j in nums2:
            if stt[j]:
                result.append(j)
            stt[j] = False
        return result
