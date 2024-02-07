class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        rst = -float('inf')
        cur_sum = 0
# whenever the current sum is < 0 drop the cur_sum to 0 ie abandone the previous sub array
        for i in range(len(nums)):
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += nums[i]
            rst = max(rst, cur_sum)

        return rst