# Problem: XOR Queries of a Subarray - https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xorPrefix = [arr[0]]
        for i in range(1, len(arr)):
            xorPrefix.append(xorPrefix[-1] ^ arr[i])
        rst = []
        for a, b in queries:
            if a == 0:
                rst.append(xorPrefix[b])
            else:
                rst.append(xorPrefix[b]^xorPrefix[a - 1])
        return rst