# Problem: Is Subsequence - https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: return True
        if not t: return False
        n, m = len(s), len(t)
        dp = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if s[i] == t[j]:
                    dp[i][j] = dp[i-1][j-1] + 1 if i > 0 and j > 0 else 1
                else:
                    if i > 0: dp[i][j] = max(dp[i][j], dp[i-1][j])
                    if j > 0: dp[i][j] = max(dp[i][j], dp[i][j-1])
        return dp[n-1][m-1] == len(s)
