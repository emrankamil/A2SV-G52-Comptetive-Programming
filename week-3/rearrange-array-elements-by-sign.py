class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        result = [0]*len(nums)
        next_positive = 0
        next_negative = 1

        for num in nums:
            if num > 0:
                result[next_positive] = num
                next_positive += 2
            else:
                result[next_negative] = num
                next_negative += 2
        
        return result
        