# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n  = len(matrix)
        for i in range(n-2, -1, -1):
            for j in range(n-1, -1, -1):
                op1 = matrix[i+1][j-1] if j > 0 else float('inf')
                op2 = matrix[i+1][j+1] if j < n - 1 else float('inf')
                matrix[i][j] += min(matrix[i+1][j], op1, op2)
        return min(matrix[0])