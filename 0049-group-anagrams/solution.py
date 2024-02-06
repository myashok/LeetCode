class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for s in strs:
            sorted_s = ''.join(sorted(s))
            group[sorted_s].append(s)         
        return list(group.values())
        

            
