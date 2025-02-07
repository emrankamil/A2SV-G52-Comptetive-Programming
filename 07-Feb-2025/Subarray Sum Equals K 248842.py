# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mapp = defaultdict(int)
        mapp[0] = 1
        count = 0
        for i in range(len(nums)):
            if i > 0: 
                nums[i] += nums[i-1]
            count += mapp[nums[i] - k]
            mapp[nums[i]] += 1

        return count