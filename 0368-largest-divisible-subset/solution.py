class Solution:
    def largestDivisibleSubset(self, arr):
        n = len(arr)
        arr.sort()
        sequence = [[num] for num in arr]
        for i in range(n):
            for j in range(i):
                if not arr[i] % arr[j] and len(sequence[i]) < len(sequence[j]) + 1:
                    sequence[i] = sequence[j] + [arr[i]]
        return max(sequence, key=len)
        
