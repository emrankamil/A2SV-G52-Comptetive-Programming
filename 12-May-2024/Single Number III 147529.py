# Problem: Single Number III - https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        x = 0
        for num in nums:
            x ^= num
        nums = set(nums)
        for num in nums:
            if num^x in nums:
                return [num, num^x]
        return []