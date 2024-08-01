# Problem: Reach a Number - https://leetcode.com/problems/reach-a-number/

class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        k = math.ceil((-1 + math.sqrt(1 + 8 * target)) / 2)
        summ = k * (k + 1) // 2
        return k if (summ - target)%2 == 0 else k + 1 + k%2
        