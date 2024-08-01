# Problem: Minimum Difference Between Largest and Smallest Value in 3 Moves - https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4: return 0
        min4 = sorted(nums[:4])
        max4 = sorted(nums[:4])

        for i in range(4, len(nums)):
            if nums[i] < min4[3]:
                min4[3] = nums[i]
                for j in range(3, 0, -1):
                    if min4[j] < min4[j - 1]:
                        min4[j], min4[j - 1] = min4[j - 1], min4[j]

            if nums[i] > max4[0]:
                max4[0] = nums[i]
                for j in range(3):
                    if max4[j] > max4[j + 1]:
                        max4[j], max4[j + 1] = max4[j + 1], max4[j]

                
        return min(max4[0]-min4[0], max4[1]-min4[1], max4[2]-min4[2], max4[3]-min4[3])

