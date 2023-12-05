class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        sum_of_ones = 0
        max_ones = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                max_ones = max(max_ones, sum_of_ones)
                sum_of_ones = 0
            sum_of_ones += nums[i]

        return max(max_ones, sum_of_ones)