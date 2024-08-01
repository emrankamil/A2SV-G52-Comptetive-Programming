# Problem: Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n, m = len(matrix), len(matrix[0])
        zero_rows, zero_cols = set(), set()

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)
        i = 0
        while i < n:
            if i in zero_rows:
                matrix[i] = [0]*m
                i += 1
                continue
            for j in range(m):
                if j in zero_cols:
                    matrix[i][j] = 0
            i += 1