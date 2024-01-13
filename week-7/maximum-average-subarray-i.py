class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        subarray_sum = sum(nums[0:k])
        max_sum = subarray_sum
        for i in range(len(nums) - k):
            next_sum = subarray_sum - nums[i] + nums[i+k]
            if next_sum > max_sum:
                max_sum = next_sum
            subarray_sum = next_sum
            
        return (max_sum/k)