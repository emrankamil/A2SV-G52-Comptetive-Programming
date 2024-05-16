# Problem: Coin Change II - https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def dp(i, target):
            if target < 0:
                return 0
            if target == 0:
                return 1
            if (i, target) not in memo:
                rst = 0
                for j in range(len(coins)):
                    if j >= i:
                        rst += dp(j, target - coins[j])
                memo[(i, target)] = rst
            return memo[(i, target)]

        return  dp(0, amount)