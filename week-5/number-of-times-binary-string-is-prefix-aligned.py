class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        currentSum = 0
        rst = 0
        maxVal = -float('inf')
        for i in range(1,len(flips)+1):
            maxVal = max(maxVal, flips[i-1])
            if i == maxVal:
                rst += 1

        return rst