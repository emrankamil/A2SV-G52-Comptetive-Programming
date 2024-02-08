class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        n, m = len(matrix[0]), len(matrix)

        prefix = [[0]*(n+1) for _ in range(m+1)]
        rst = 0
        for i in range(1,m+1):
            for j in range(1,n+1):
                cur_sum = prefix[i-1][j]+prefix[i][j-1]-prefix[i-1][j-1]+matrix[i-1][j-1]
                for k in range(i):
                    for l in range(j):
                        if cur_sum-prefix[k][j]-prefix[i][l]+prefix[k][l] == target:
                            rst += 1
                prefix[i][j] = cur_sum
        return rst