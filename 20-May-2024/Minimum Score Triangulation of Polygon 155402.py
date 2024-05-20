# Problem: Minimum Score Triangulation of Polygon - https://leetcode.com/problems/minimum-score-triangulation-of-polygon/

class Solution(object):
    def minScoreTriangulation(self, values):
        @cache
        def dfs(left, right):
            if right - left + 1 < 3:
                return 0
            minnum = float("Inf")
            for k in range(left+1, right):
                minnum = min(minnum, values[left]*values[right]*values[k] + dfs(left, k) + dfs(k, right))
            return minnum
        return dfs(0, len(values) - 1)