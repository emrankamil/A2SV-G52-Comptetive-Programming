# Problem: Maximum Gap - https://leetcode.com/problems/maximum-gap/

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return abs(nums[-1] - nums[0])

        stores = [[] for _ in range(10)]
        digits = len(str(max(nums)))

        for i in range(digits):
            for num in nums:
                idx = (num//(10**i))%10
                stores[idx].append(num)
            index = 0
            for k in range(10):
                for val in stores[k]:
                    nums[index] = val
                    index += 1
                stores[k] = []
            
        max_gap = 0
        for i in range(1, len(nums)):
            max_gap = max(max_gap, nums[i]-nums[i-1])
        return max_gap