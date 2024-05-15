# Problem: Integer Break - https://leetcode.com/problems/integer-break/

class Solution:
    def integerBreak(self, n: int) -> int:
        @cache
        def dp(i):
            if i == 2:
                return 1
            rst = 1
            for j in range(i-2, -1, -1):
                rst = max(rst, dp(j) * (i-j))
            return rst
        if n <= 3:
            return n-1
        return dp(n)