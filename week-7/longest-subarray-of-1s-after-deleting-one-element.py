class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        if 0 in nums:
            last_index = nums.index(0)
        else:
            return len(nums)-1
        
        rst, left = 0,0
        for i in range(last_index+1,len(nums)):
            if nums[i] == 0:
                rst = max(rst,i-left-1)
                left = last_index+1
                last_index = i
        return max(rst, len(nums)-left-1)
            