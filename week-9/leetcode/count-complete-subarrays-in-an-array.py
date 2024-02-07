class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        m ,n,left = len(nums), len(set(nums)),0
        hashMap = {}
        result = 0
        for i in range(len(nums)):
            if nums[i] in hashMap:
                hashMap[nums[i]] += 1
            else:
                hashMap[nums[i]] = 1
            
            while len(hashMap) == n:
                result += m-i
                if hashMap[nums[left]] == 1:
                    del hashMap[nums[left]]
                else:
                    hashMap[nums[left]] -= 1
                left += 1

        return result
        