class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)-1
        while low < high:
            mid = (low+high)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                low = mid+1
            else:
                high = mid
        if nums[low] < target:
            return low+1
        return low