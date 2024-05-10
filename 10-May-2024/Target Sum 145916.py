# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = defaultdict(tuple)
        def dp(i, target):
            if i >= len(nums):
                if target == 0:
                    return 1
                return 0
            if (i, target) not in memo:
                cur = dp(i + 1, target-nums[i]) + dp(i+1, target + nums[i])
                memo[(i, target)] = cur
            return memo[(i, target)]
        
        return dp(0, target)