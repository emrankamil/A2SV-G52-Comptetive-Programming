# Problem: Pass the Pillow - https://leetcode.com/problems/pass-the-pillow/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        div, mod = time // (n - 1), time % (n-1)
        if div % 2: 
            return n - mod
        else:
            return mod + 1