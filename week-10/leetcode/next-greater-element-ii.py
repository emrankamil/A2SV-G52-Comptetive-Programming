class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        n = len(nums)
        rst = [-1]*n
        for i in range(2*len(nums)):
            i %= n
            while stack and nums[ stack[-1] ] < nums[i]:
                rst[stack.pop()] = nums[i]
            stack.append(i)
        return rst