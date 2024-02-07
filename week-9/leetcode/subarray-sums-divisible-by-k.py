class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        prefix[0]= 1
        rst = 0

        for i in range(len(nums)):
            if i!=0:
                nums[i] += nums[i-1]
            rst += prefix[nums[i]%k]
            prefix[nums[i]%k] += 1

        return rst
        
        