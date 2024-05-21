# Problem: Dungeon Game - https://leetcode.com/problems/dungeon-game/

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        @cache
        def dp(i, j):
            if i >= m or j >= n:
                return float('inf')
            if i == m-1 and j == n-1:
                if dungeon[-1][-1] <= 0:
                    return -dungeon[-1][-1] + 1
                return 1
            right = dp(i, j + 1)
            down = dp(i + 1, j)

            req = min(right, down) - dungeon[i][j]
            return req if req > 0 else 1

        return dp(0, 0)