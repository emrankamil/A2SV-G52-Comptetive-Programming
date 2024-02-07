class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        check = defaultdict(int)
        check[0] = 1
        rst = 0
        for i in range(len(nums)):
            if i!= 0:
                nums[i] += nums[i-1]
            if nums[i]-k in check:
                rst += check[nums[i]-k]
            check[nums[i]] += 1

        return rst
