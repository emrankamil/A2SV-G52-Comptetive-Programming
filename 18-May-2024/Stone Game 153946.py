# Problem: Stone Game - https://leetcode.com/problems/stone-game/

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @cache
        def dp(i, j):
            if i == j:
                return piles[i]
            if i + 1 == j:
                return max(piles[i], piles[j])
            return max(dp(i+1, j) + piles[i], dp(i, j-1) + piles[j])
        total, n = sum(piles), len(piles)
        return 2 * dp(0, n-1) > total