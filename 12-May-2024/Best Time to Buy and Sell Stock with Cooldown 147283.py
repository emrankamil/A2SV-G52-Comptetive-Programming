# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = defaultdict(tuple)
        def dp(i, state): # sell: 1, buy: 0
            if i >= len(prices):
                return 0
            if (i, state) not in memo:
                rst = 0
                if state == 1:
                    rst = max(rst, dp(i+2, 0)+prices[i], dp(i+1, 1))
                else:
                    rst = max(rst, dp(i+1, 1)-prices[i], dp(i+1, 0))
                memo[(i, state)] = rst
            return memo[(i, state)]
        return dp(0, 0)