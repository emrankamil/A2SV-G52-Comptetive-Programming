class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        rst = []
        left = 0
        right = left+n//3
        while left < (n-n//3):
            if nums[left] == nums[left+n//3] and nums[left] not in rst:
                rst.append(nums[left])
                left = right+1
                right = left+n//3
            else:
                left += 1
                right += 1
            if len(rst) == 2:
                return rst

        return rst
