# Problem: Frog Jump - https://leetcode.com/problems/frog-jump/

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        @cache
        def dp(prev, i):
            if i >= n:
                return False
            if i == n - 1:
                return True
            start = max(i + 1, bisect_left(stones, prev - 1))
            next_jumps = {prev - 1, prev, prev + 1}
            for j in range(start, n):
                jump = stones[j] - stones[i]
                if jump > prev + 1:
                    return False
                if jump in next_jumps and dp(jump, j):
                    return True
            return False
        return dp(0, 0)