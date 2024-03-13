class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        cur_sum = []
        for i in range(1, len(weights)):
            cur_sum.append(weights[i]+weights[i-1])
        cur_sum.sort()
        n = len(cur_sum)
        
        return sum(cur_sum[n-k+1:n])-sum(cur_sum[:k-1])