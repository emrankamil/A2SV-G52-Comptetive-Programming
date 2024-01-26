class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefixSum = [0]*len(nums)
        mp = {}
        for i in range(len(nums)):
            prefixSum[i]= (prefixSum[i-1] + nums[i]) % k
        for i in prefixSum:
            if i in mp:
                mp[i] += 1
            else:
                mp[i] = 1
        output = 0
        for i in mp:
            combination = (mp[i] *( mp[i] - 1))//2
            if i == 0:
                output += mp[i] + combination
            else:
                output += combination
        
        return output
                
                
        
        
        