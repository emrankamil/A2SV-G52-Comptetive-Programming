# Problem: Most Profit Assigning Work - https://leetcode.com/problems/most-profit-assigning-work/

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:

        zipp = list(zip(difficulty, profit))
        zipp.sort()
        worker.sort()
        i, max_profit, rst = 0, 0, 0

        for w in worker:
            while i < len(zipp) and zipp[i][0] <= w:
                max_profit = max(max_profit, zipp[i][1])
                i += 1
            rst += max_profit
        return rst
        