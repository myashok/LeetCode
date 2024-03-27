class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        sqrt_n = int(math.sqrt(n))
        factors = set()
        for i in range(1, sqrt_n + 1):
            if n % i == 0:
                factors.add(i)
                factors.add(n//i)
        if len(factors) < k:
            return -1
        factors = sorted(list(factors))
        return factors[k-1]
