class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        cur_max, cur_sum = nums[0], nums[0]

        for i in range(1, len(nums)):
            cur_sum += nums[i]
            cur_max = max(cur_max, (cur_sum+i)//(i+1))
        return cur_max