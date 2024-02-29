class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        lastVal = nums[-1]
        rst = 0
        for i in range(len(nums)-2,-1,-1):
            if nums[i]>lastVal:
                div = nums[i]//lastVal
                mod = nums[i]%lastVal

                if mod:
                    rst += div
                    lastVal= nums[i]//(div+1)
                else:
                    rst += div-1
                    lastVal = nums[i]//(div)
            else:
                lastVal = nums[i]
        return rst