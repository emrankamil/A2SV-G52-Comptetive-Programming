# Problem: Count Collisions of Monkeys on a Polygon - https://leetcode.com/problems/count-collisions-of-monkeys-on-a-polygon/

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

    def monkeyMove(self, n: int) -> int:
        k = self.myPow(2, n) - 2
        mod = pow(10, 9) + 7
        if k < 0: return mod - 1
        return k
