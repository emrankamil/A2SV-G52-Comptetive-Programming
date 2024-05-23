# Problem: Triangle - https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}
        def dp(i, j):
            if i >= len(triangle) or j >= len(triangle[i]):
                return 0
            if (i, j) not in memo:
                rst = min(dp(i + 1, j), dp(i + 1, j + 1))
                memo[(i, j)] = rst + triangle[i][j] 
            return memo[(i, j)]
        return dp(0, 0)