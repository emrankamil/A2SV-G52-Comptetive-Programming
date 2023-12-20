class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        prefixMatrix = [[0]*(len(grid[0])+1) for i in range(len(grid)+1)]
        rst = float('-inf')

        for i in range(1, len(prefixMatrix)):
            for j in range(1, len(prefixMatrix[0])):
                prefixMatrix[i][j]=(
                    prefixMatrix[i-1][j]
                    +prefixMatrix[i][j-1]
                    +grid[i-1][j-1
                    ]-prefixMatrix[i-1][j-1])
                    
                if i>=3 and j>=3:
                    hourGlassSum = (
                    prefixMatrix[i][j]-
                    prefixMatrix[i-3][j]-
                    prefixMatrix[i][j-3]+
                    prefixMatrix[i-3][j-3]-
                    grid[i-2][j-1]-
                    grid[i-2][j-3]
                    )
                    rst = max(rst, hourGlassSum)

        return rst

                