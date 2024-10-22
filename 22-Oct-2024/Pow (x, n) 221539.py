# Problem: Pow (x, n) - https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n *= -1
            x = 1/x
        rst = 1
        while n > 0:
            if n & 1:
                rst *= x
            x *= x
            n >>= 1
        return rst