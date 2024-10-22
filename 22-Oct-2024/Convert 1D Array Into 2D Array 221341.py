# Problem: Convert 1D Array Into 2D Array - https://leetcode.com/problems/convert-1d-array-into-2d-array/

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        rst = []
        cur = 0
        for _ in range(m):
            row = []
            for _ in range(n):
                if cur == len(original):
                    return []
                row.append(original[cur])
                cur += 1
            rst.append(row)
        if cur == len(original):
            return rst
        return []