class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        currentCount = sum(nums)
        maxCount = currentCount
        output = [0]
        for i in range(len(nums)):
            if nums[i] == 0:
                currentCount += 1
                if currentCount > maxCount:
                    maxCount = currentCount
                    output = [i+1]
                elif currentCount == maxCount:
                    output.append(i+1)
            else:
                currentCount -= 1
        return output