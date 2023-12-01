class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        mp = {}
        identicals = 0
        for num in nums:
            if num in mp:
                identicals += mp[num]
                mp[num] += 1
            else:
                mp[num] = 1
        return identicals