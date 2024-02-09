class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prefix = [0]*len(nums)
        suffix = [0]*len(nums)
        n = len(nums)

        for i in range(1,n):
            prefix[i] = prefix[i-1]+i*(nums[i]-nums[i-1])
            suffix[n-i-1] = suffix[n-i] + i*(nums[n-i]-nums[n-i-1])

        for i in range(len(nums)):
            nums[i] = prefix[i]+suffix[i]
            
        return nums