# Problem: Best Time to Buy and Sell Stock with Transaction Fee - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy, sell = -prices[0], 0
        for i in range(1, len(prices)):
            buy = max(buy, sell-prices[i])
            sell = max(sell, buy+prices[i]-fee)
        return sell