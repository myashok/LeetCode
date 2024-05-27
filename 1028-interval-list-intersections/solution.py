class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        m = len(firstList)
        n = len(secondList)
        i = j = 0
        ans = []
        while i < m and j < n:
            if firstList[i][1] >=  secondList[j][0] and secondList[j][1] >= firstList[i][0]:
                ans.append([max(firstList[i][0], secondList[j][0]), min(firstList[i][1],secondList[j][1])])
            if firstList[i][1] <= secondList[j][1]:
                i += 1
            else: 
                j += 1
        return ans


        
