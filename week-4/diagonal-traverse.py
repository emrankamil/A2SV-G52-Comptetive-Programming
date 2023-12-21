class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n , m = len(mat), len(mat[0])
        reverse = False
        result = []
        for i in range(n):
            diagonal = []
            row = i
            column = i-row # here i can be considered as the sum of col and row and in case of diagonal those sums are constant.
            while row >= 0 and column < m:
                diagonal.append(mat[row][column])
                row -= 1
                column += 1
            if reverse:
                result.extend(reversed(diagonal))
            else:
                result.extend(diagonal)
            reverse = not reverse

        for i in range(1,m):
            diagonal = []
            column = i
            row = n-1 # here i can be considered as the sum of col and row and in case of diagonal those sums are constant.
            while row >= 0 and column < m:
                diagonal.append(mat[row][column])
                row -= 1
                column += 1
            if reverse:
                result.extend(reversed(diagonal))
            else:
                result.extend(diagonal)
            reverse = not reverse
        return result