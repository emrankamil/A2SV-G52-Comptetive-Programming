class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, val in enumerate(nums):
            x = i + 1
            while x != len(nums):
                if (nums[i] + nums[x]) == target:
                    return [i, x]
                else:
                    x += 1
        
        return []  # If no solution is found

obj = Solution()