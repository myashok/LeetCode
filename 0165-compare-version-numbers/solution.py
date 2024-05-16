class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        splitted1 = version1.split('.')
        splitted2 = version2.split('.')
        for i in range(max(len(splitted1), len(splitted2))):
            v1 = int(splitted1[i]) if i < len(splitted1) else 0
            v2 = int(splitted2[i]) if i < len(splitted2) else 0
            if v1 < v2:
                return -1
            elif v1 > v2:
                return 1
        return 0
