# Problem: Best Time to Buy and Sell Stock III - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dp(i, state, transactions):
            if i >= len(prices) or transactions == 0:
                return 0
            if state == 'buy':
                op1 = dp(i + 1, 'sell', transactions) - prices[i]
                op2 = dp(i + 1, 'buy', transactions)
                return max(op1, op2)
            else:
                op1 = dp(i + 1, 'buy', transactions - 1) + prices[i]
                op2 = dp(i + 1, 'sell', transactions)
                return max(op1, op2)
        return dp(0, 'buy', 2)