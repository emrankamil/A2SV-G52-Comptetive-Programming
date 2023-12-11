class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        check = True
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                if not check:
                    return False
                if i>=2 and nums[i-2]>nums[i]:
                    nums[i]=nums[i-1]
                check = False
        return True