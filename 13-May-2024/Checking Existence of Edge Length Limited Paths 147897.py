# Problem: Checking Existence of Edge Length Limited Paths - https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * (n)
    
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
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

class Solution:
    def distanceLimitedPathsExist(self, n, edgeList, queries):
        q = [(limit, u, v, i) for i, (u, v, limit) in enumerate(queries)]
        edgeList.sort(key=lambda x:x[2])
        q.sort()
        uf = UnionFind(n)
        result = [False]*len(queries)
        cur = 0
        for limit, u, v, i in q:
            while cur < len(edgeList) and edgeList[cur][2] < limit:
                uf.union(edgeList[cur][0], edgeList[cur][1])
                cur += 1
            result[i] =( uf.find(u) == uf.find(v))
        return result
