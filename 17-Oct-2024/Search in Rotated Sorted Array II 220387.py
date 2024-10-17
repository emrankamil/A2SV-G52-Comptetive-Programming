# Problem: Search in Rotated Sorted Array II - https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            mid = l + (r - l)//2
            print(mid, nums[mid], target)
            if nums[mid] == target:
                return True
            if nums[mid] == nums[l]:
                l += 1
            elif nums[l] < nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid
                else:
                    l = mid
            elif nums[mid] <= target <= nums[r]:
                l = mid
            else:
                r = mid
        return l < n and nums[l] == target
            