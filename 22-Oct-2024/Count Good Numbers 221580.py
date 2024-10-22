# Problem: Count Good Numbers - https://leetcode.com/problems/count-good-numbers/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        mod = pow(10, 9) + 7
        rst = 1
        while n > 0:
            if n & 1:
                rst = (rst * x) % mod
            x = (x * x) % mod
            n >>= 1
        return rst % mod

    def countGoodNumbers(self, n: int) -> int:
        k = self.myPow(20, n//2)
        mod = 10**9 + 7
        if n % 2 == 0:
            return k
        else:
            return (5 * k) % mod