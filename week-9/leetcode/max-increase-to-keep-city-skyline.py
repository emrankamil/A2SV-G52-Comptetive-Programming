class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row_max = [0]*n
        col_max = [0]*n

        for i in range(n):
            for j in range(n):
                row_max[i] = max(row_max[i], grid[i][j])
                col_max[j] = max(col_max[j], grid[i][j])
        rst = 0
        for i in range(n):
            for j in range(n):
                change = min(row_max[i],col_max[j])
                rst += abs(change-grid[i][j])
    
        return rst
        