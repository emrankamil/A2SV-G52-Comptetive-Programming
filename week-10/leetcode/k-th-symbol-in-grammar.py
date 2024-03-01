class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n==1: return 0
        if k <= pow(2,n-2):
            return self.kthGrammar(n-1, k)
        return int(not self.kthGrammar(n-1, k-pow(2,n-2)))

# n = 1 | 0 -- 2^0 elements
# n = 2 | 01 -- 2^1 elements
# n = 3 | 01 10 -- 2^2 elements
# n = 4 | 01 10 1001 -- 2^3 elements
# n = 5 | 01 10 1001 10010110 -- 2^4 elements