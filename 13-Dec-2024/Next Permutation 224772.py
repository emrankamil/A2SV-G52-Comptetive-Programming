# Problem: Next Permutation - https://leetcode.com/problems/next-permutation/description/

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        n = len(nums)
        i = n - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        
        if i >= 0:
            j = i + 1
            while j < n and nums[j] > nums[i]:
                j += 1
            nums[j-1], nums[i] = nums[i], nums[j-1]
            reverse(i + 1, n - 1)
        else:
            reverse(0, n - 1)

        return nums
            
