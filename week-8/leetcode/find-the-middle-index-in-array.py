class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefix_sum1 = [0]*len(nums)
        prefix_sum2 = [0]*len(nums)

        prefix_sum1[0] = nums[0]
        prefix_sum2[-1] = nums[-1]

        for i in range(1, len(nums)):
            prefix_sum1[i] = prefix_sum1[i - 1] + nums[i]
            prefix_sum2[len(nums) - 1 - i] = prefix_sum2[len(nums) - i] + nums[len(nums) - 1 - i]


        for i in range(len(nums)):
            if prefix_sum1[i]==prefix_sum2[i]:
                return i
        return -1