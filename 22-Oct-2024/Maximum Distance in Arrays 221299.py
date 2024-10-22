# Problem: Maximum Distance in Arrays - https://leetcode.com/problems/maximum-distance-in-arrays/

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        arrays.sort()
        rst = 0
        for i in range(1, len(arrays)):
            rst = max(rst, abs(arrays[i][-1] - arrays[0][0]))
        return max(rst, abs(arrays[0][-1] - arrays[1][0]))
        