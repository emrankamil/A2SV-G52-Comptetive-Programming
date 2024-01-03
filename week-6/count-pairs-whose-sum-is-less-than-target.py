class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        left = 0
        right = len(nums)-1
        rst = 0
        
        while right > left:
            if nums[right]+nums[left] >= target:
                right -= 1
            else:
                rst += (right-left)
                left += 1

        return rst