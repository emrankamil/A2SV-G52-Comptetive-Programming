class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n, m = len(matrix), len(matrix[0])
        rst = []
        for i in range(m):
            rst.append([])
            for j in range(n):
                rst[-1].append(matrix[j][i])
        return rst
                    
        