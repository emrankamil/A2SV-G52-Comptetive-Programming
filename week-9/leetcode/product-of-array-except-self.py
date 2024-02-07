class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefixProduct = [1] * n
        suffixProduct = [1] * n
        rst = [0] * n

        # Calculate prefix products
        prefix = 1
        for i in range(n):
            prefixProduct[i] = prefix
            prefix *= nums[i]

        # Calculate suffix products
        suffix = 1
        for i in range(n - 1, -1, -1):
            rst[i] = prefixProduct[i] * suffix
            suffix *= nums[i]

        return rst

        
        