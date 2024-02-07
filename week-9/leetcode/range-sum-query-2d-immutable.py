class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i==0 and j==0:
                    continue
                elif i==0:
                    matrix[i][j] += matrix[i][j-1]
                elif j==0:
                    matrix[i][j] += matrix[i-1][j]
                else:
                    matrix[i][j] += (matrix[i][j-1]+matrix[i-1][j]-matrix[i-1][j-1])
        self.NumMatrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1==0 and col1==0:
            return self.NumMatrix[row2][col2]
        elif row1==0:
            return self.NumMatrix[row2][col2]-self.NumMatrix[row2][col1-1]
        elif col1==0:
            return self.NumMatrix[row2][col2]-self.NumMatrix[row1-1][col2]
        return self.NumMatrix[row2][col2]-self.NumMatrix[row2][col1-1]-self.NumMatrix[row1-1][col2]+self.NumMatrix[row1-1][col1-1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)