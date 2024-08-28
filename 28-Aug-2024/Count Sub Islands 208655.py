# Problem: Count Sub Islands - https://leetcode.com/problems/count-sub-islands/

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n, res = len(grid1), len(grid1[0]), 0
        
        def dfs(r, c):
            if r < 0 or c < 0 or r == m or c == n or grid2[r][c] == 0:
                return True
            elif grid2[r][c] != grid1[r][c]:
                return False
            grid2[r][c] = 0
            return dfs(r+1, c) & dfs(r-1, c) & dfs(r, c+1) & dfs(r, c-1)

        count = 0
        for i in range(m):
            for j in range(n):
                if grid1[i][j] + grid2[i][j] == 2:
                    count += dfs(i, j)
        return count