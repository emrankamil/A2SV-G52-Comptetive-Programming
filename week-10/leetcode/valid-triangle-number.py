class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        rst = 0
        for k in range(2, len(nums)):
            i, j = 0, k-1
            while j>i:
                if nums[i] + nums[j] > nums[k]:
                    rst += j-i
                    j -= 1
                else:
                    i += 1
        return rst