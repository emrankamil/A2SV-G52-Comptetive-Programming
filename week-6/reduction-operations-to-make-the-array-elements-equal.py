class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        distinctNums = 0
        rst = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                distinctNums += 1
            rst += distinctNums

        return rst
