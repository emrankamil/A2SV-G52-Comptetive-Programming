# Problem: IPO - https://leetcode.com/problems/ipo/

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        max_heap = []
        min_heap = [(c, p) for c,p in zip(capital, profits)]
        heapify(min_heap)
        for i in range(k):
            while min_heap and min_heap[0][0] <= w:
                c, p = heappop(min_heap)
                heappush(max_heap, -p)
            if not max_heap:
                break
            profit = heappop(max_heap)
            w += -profit
        return w