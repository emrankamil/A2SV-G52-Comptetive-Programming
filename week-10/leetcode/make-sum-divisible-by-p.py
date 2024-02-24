class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        k = sum(nums) % p
        if (k == 0):
            return 0

        minLength = lengthNums = len(nums)
        currSum, dictLengths = 0, defaultdict(lambda : 0)
        for i in range(lengthNums):
            currSum = (currSum + nums[i]) % p
            if (currSum == k):
                minLength = min(minLength, i+1)

            if ((currSum - k) % p in dictLengths):
                minLength = min(minLength, i - dictLengths[(currSum - k) % p])

            dictLengths[currSum] = i

        return minLength if (minLength < lengthNums) else -1