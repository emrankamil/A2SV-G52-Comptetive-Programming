class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        rst = 0

        for i in range(len(nums)):
            if i != 0:
                nums[i] += nums[i-1]
            if nums[i]-goal>=0:
                rst += prefix[nums[i]-goal] 
            prefix[nums[i]] += 1
            
        return rst