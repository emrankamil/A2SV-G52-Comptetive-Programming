class Solution:
    def numberOfMatches(self, n: int) -> int:
        rst = 0
        while n > 1:
            rst += n//2
            n -= n//2
        return rst