class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        minVal = nums[0]
        minArr = [0]*(len(nums))
        for i in range(1, len(nums)-1):
            if nums[i] > minVal:
                minArr[i] = 1
            else:
                minVal = nums[i]
                minArr[i] = 0

        maxVal = nums[len(nums)-1]
        for j in range(len(nums)-2,0,-1):
            if nums[j] >= maxVal:
                maxVal = nums[j]
            elif minArr[j] == 1:
                return True
        
        return False
        