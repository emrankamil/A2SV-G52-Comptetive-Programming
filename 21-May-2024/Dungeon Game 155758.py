# Problem: Dungeon Game - https://leetcode.com/problems/dungeon-game/

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        dp = [[0] * n for _ in range(m)]
        dp[-1][-1] = 1 if dungeon[-1][-1] >= 0 else -dungeon[-1][-1] + 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1: continue
                right = dp[i][j+1] if j + 1 < n else float('inf')
                down = dp[i+1][j] if i + 1 < m else float('inf')
                req_min_health = min(right, down) - dungeon[i][j] 
                if req_min_health > 0:
                    dp[i][j] = req_min_health
                else:
                    dp[i][j] = 1
        return dp[0][0]
