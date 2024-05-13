# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indegree = [0]*n
        for u, v in edges:
            indegree[v] += 1
        rst = -1
        for i, val in enumerate(indegree):
            if val == 0:
                if rst >= 0:
                    return -1
                else:
                    rst = i
        return rst