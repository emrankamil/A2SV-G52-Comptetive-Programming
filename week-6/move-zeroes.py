class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if 0 in nums:
            ph = nums.index(0)
        else:
            return
        for i in range(ph+1, len(nums)):
            if nums[i] != 0:
                nums[ph], nums[i] = nums[i], nums[ph]
                ph += 1

     