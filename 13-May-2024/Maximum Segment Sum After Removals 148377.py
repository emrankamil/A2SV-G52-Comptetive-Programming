# Problem: Maximum Segment Sum After Removals - https://leetcode.com/problems/maximum-segment-sum-after-removals/description/

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * (n)
        self.segment_sum = defaultdict(int)
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x]) 
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return
        
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
            self.segment_sum[root_y] += self.segment_sum[root_x]
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
            self.segment_sum[root_x] += self.segment_sum[root_y]
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
            self.segment_sum[root_x] += self.segment_sum[root_y]

class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        n = len(nums)
        uf = UnionFind(n)
        result = [0]*n
        max_sum = 0
        for i in range(n-1, -1, -1):
            result[i] = max_sum
            q = removeQueries[i]
            uf.segment_sum[q] = nums[q]
            if q - 1 in uf.segment_sum: uf.union(q-1, q)
            if q + 1 in uf.segment_sum: uf.union(q, q+1)
            root_q = uf.find(q)
            max_sum = max(max_sum , uf.segment_sum[root_q])
        return result