class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x:(x[0]-x[1]))
        rst=0
        for i in range(len(costs)):
            if i<len(costs)//2:
                rst += costs[i][0]
            else:
                rst += costs[i][1]

        return rst