class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_good = len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if i+nums[i]>=last_good:
                last_good = i
        return last_good==0