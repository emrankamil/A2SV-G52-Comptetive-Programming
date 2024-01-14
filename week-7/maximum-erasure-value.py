class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        current_sum = 0
        left = 0
        max_sum = 0
        for i in range(len(nums)):
            while mp[nums[i]] > 0:
                mp[nums[left]] -= 1
                current_sum -= nums[left]
                left += 1
            mp[nums[i]] += 1
            current_sum += nums[i]  
            max_sum = max(max_sum, current_sum)
        return max_sum