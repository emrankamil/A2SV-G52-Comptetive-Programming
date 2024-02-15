class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patches = 0
        totalCoverage = 0
        i=0
        while totalCoverage < n:
            if i>=len(nums) or nums[i]>totalCoverage+1:
                patches += 1
                totalCoverage += (totalCoverage+1)
            else:
                totalCoverage += nums[i]
                i +=1
        return patches