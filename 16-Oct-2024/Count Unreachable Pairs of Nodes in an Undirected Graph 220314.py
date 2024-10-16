# Problem: Count Unreachable Pairs of Nodes in an Undirected Graph - https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

class DisjSet: 
	def __init__(self, n): 
		self.rank = [1] * n 
		self.parent = [i for i in range(n)] 


	def find(self, x): 
		if (self.parent[x] != x): 
			self.parent[x] = self.find(self.parent[x]) 
		return self.parent[x] 

	def Union(self, x, y): 
		xset = self.find(x) 
		yset = self.find(y) 

		# If they are already in same set 
		if xset == yset: 
			return

		if self.rank[xset] < self.rank[yset]: 
			self.parent[xset] = yset 

		elif self.rank[xset] > self.rank[yset]: 
			self.parent[yset] = xset 

		else: 
			self.parent[yset] = xset 
			self.rank[xset] = self.rank[xset] + 1


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        ds = DisjSet(n)
        for a, b in edges:
            ds.Union(a, b)
        count = defaultdict(int)
        for i in range(n):
            i_parent = ds.find(i)
            count[i_parent] += 1
        cur_sum = 0
        rst = 0
        for i in count:
            rst += count[i]*cur_sum
            cur_sum += count[i]

        return rst