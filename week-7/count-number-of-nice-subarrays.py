class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        cumulative = 0
        rst = 0
        mp = {0:1}
        for i in range(len(nums)):
            cumulative += nums[i]%2
            diff_from_k = cumulative-k

            if diff_from_k in mp:
                rst += mp[diff_from_k]
            if cumulative in mp:
                mp[cumulative] += 1
            else:
                mp[cumulative] = 1

        return rst

        

            