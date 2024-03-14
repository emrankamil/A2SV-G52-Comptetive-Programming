class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low, high = 0, len(nums)-1
        rst = [-1, -1]
        while low < high:
            mid = (low+high)//2
            if nums[mid] >= target:
                high = mid
            else:
                low = mid+1
        if low < len(nums) and nums[low] == target:
            rst[0] = low
        else:
            return [-1, -1]
        high = len(nums)-1
        while low < high:
            mid = (low+high+1)//2
            if nums[mid] <= target:
                low = mid
            else:
                high = mid-1
        rst[1] = low
        return rst