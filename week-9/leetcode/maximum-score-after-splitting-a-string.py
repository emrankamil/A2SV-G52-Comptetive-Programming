class Solution:
    def maxScore(self, s: str) -> int:
        prefix = [0]*(len(s))
        total_sum = 0
        for i in range(len(s)):
            prefix[i] = prefix[i-1]+int(s[i])
            total_sum += int(s[i])
        rst = 0
        for i in range(len(prefix)-1):
            left_zeros = i-prefix[i]+1
            right_ones = total_sum-prefix[i]
            rst = max(rst, left_zeros+right_ones)
        return rst