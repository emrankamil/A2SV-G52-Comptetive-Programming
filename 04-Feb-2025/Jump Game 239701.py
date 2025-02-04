# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cur_max = 0
        for i in range(len(nums)-1):
            cur_max = max(cur_max - 1, nums[i])
            if cur_max == 0:
                return False
        return True