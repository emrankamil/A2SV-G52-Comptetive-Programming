class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        sorted_nums = sorted(nums)
        
        count= {}
        for i,val in enumerate(sorted_nums):
            if val not in count:
                count[val] = i


        for i, val in enumerate(nums):
            nums[i] = count[val]
        
        return nums