# Problem: Maximum XOR for Each Query - https://leetcode.com/problems/maximum-xor-for-each-query/

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        nums[0] ^= 2**maximumBit - 1
        for i in range(1, len(nums)):
            nums[i] ^= nums[i-1]
        return nums[::-1]