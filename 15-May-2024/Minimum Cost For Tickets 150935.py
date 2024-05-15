# Problem: Minimum Cost For Tickets - https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo = {}

        def dp(cur_day):
            if cur_day > days[-1]:
                return 0
            if cur_day not in _set:
                return dp(cur_day + 1)
            if cur_day not in memo:
                op1 = dp(cur_day + 1) + costs[0]
                op2 = dp(cur_day + 7) + costs[1] 
                op3 = dp(cur_day + 30) + costs[2]
                memo[cur_day] = min(op1, op2, op3)
            return memo[cur_day]
        _set = set(days)
        return dp(days[0])