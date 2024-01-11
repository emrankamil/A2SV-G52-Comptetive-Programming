class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        current_sum = 0
        rst = float('inf')
        for r in range(len(nums)):
            current_sum += nums[r]
            while current_sum >= target:
                rst = min(rst, r-left+1)
                current_sum -= nums[left]
                left += 1

        if rst == float('inf'):
            return 0
        return rst
        