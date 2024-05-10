# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = defaultdict(int)
        def dp(target):
            if target < 0:
                return float('inf')
            if target == 0:
                return 0
            if target not in memo:
                rst = float('inf')
                for i in coins:
                    rst = min(float('inf'), dp(target-i), rst)
                memo[target] = rst+1

            return memo[target]
        rst = dp(amount)
        return -1 if rst == float('inf') else rst
