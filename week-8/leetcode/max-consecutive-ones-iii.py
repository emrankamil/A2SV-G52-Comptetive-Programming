class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
#increment your right pointer as long as k is not -1, if you have found 0 in your
#way decrement k, if k==-1 increment the left
#pointer to return k back to 0 and then we will proceed incrementing the right pointer
        left = 0
        rst = 0
        for i in range(len(nums)):
            if nums[i]==0:
                k -= 1
            if k == -1:
                rst = max(rst, i-left)
            while k == -1:
                if nums[left]==0:
                    k += 1
                left += 1

        return max(rst, len(nums)-left)
            
           
                