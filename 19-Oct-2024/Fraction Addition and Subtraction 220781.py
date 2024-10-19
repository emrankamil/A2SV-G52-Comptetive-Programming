# Problem: Fraction Addition and Subtraction - https://leetcode.com/problems/fraction-addition-and-subtraction/

class Solution:
    def addFraction(self, a, b, c, d):
        lcm_bd = lcm(b, d)
        numn = a*(lcm_bd//b) + c*(lcm_bd//d)
        gcf = gcd(numn, lcm_bd)
        return numn//gcf, lcm_bd//gcf

    def fractionAddition(self, expression: str) -> str:
        exp = expression.split("/")
        a, b = 0, 1
        for i in range(len(exp)-1):
            c = int(exp[i])
            if "+" in exp[i+1]:
                idx = exp[i+1].index("+")
                d = int(exp[i+1][:idx])
                exp[i+1] = exp[i+1][idx+1:]
            elif "-" in exp[i+1]:
                idx = exp[i+1].index("-")
                d = int(exp[i+1][:idx])
                exp[i+1] = exp[i+1][idx:]
            else:
                d = int(exp[i+1])

            a, b = self.addFraction(a, b, c, d)
        return str(a)+"/"+str(b)