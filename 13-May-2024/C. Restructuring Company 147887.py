# Problem: C. Restructuring Company - https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/C

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n+1)]
        self.rank = [0] * (n+1)
        self.next_disjoint = [i+1 for i in range(n+1)] # initially the next disjoint value of all i is i+1
    
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

    def union_range(self, x, y):
        while x < y:
            self.union(x,y)
            temp = self.next_disjoint[x]
            self.next_disjoint[x] = self.next_disjoint[y]
            x = temp
             # Update the value of x to the next disjoint value and
             # set the next disjoint value of x to the next disjoint value of y

n, q = map(int, input().split())
uf = UnionFind(n)
for _ in range(q):
    type, x, y = map(int, input().split())
    if type == 1:
        uf.union(x,y)
    elif type == 2:
        uf.union_range(x,y)
    else:
        if uf.find(x) == uf.find(y):
            print('YES')
        else:
            print('NO')