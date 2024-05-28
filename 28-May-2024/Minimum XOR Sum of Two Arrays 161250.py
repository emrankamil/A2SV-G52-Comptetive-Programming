# Problem: Minimum XOR Sum of Two Arrays - https://leetcode.com/problems/minimum-xor-sum-of-two-arrays/

from typing import List

class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        xor_matrix = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                xor_matrix[i][j] = nums1[i] ^ nums2[j]
        
        @cache
        def dp(i, visited):
            if i >= n: 
                return 0
            
            next_min = float('inf')
            for j in range(n):
                if visited & (1 << j):
                    new_visited = visited & ~(1 << j)
                    val = dp(i + 1, new_visited) + xor_matrix[i][j]
                    next_min = min(val, next_min)
            return next_min

        return dp(0, (1 << n) - 1)
