# Problem: Unique Paths II - https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[m-1][n-1]: return 0
        
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j]: continue
                dp[i][j] += dp[i-1][j] if i > 0 and not obstacleGrid[i-1][j] else 0
                dp[i][j] += dp[i][j-1] if j > 0 and not obstacleGrid[i][j-1] else 0
        return dp[m-1][n-1]