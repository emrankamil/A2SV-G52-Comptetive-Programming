class Solution:
    def isHappy(self, n: int) -> bool:
        checked = set()
        while n not in checked and n <= 2**31 - 1:
            checked.add(n)
            strN = str(n)
            n = 0
            for i in range(len(strN)):
                n += (int(strN[i]))**2
            if n == 1:
                return True
        return False