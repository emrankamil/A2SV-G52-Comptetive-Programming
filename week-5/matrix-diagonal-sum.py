class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        rst = 0
        n = len(mat)
        for i in range(n):
            for j in range(n):
                if i==j or i+j == n-1:
                    rst += mat[i][j]
        return rst