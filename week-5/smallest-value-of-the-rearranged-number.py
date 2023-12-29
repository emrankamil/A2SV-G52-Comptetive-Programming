class Solution:
    def smallestNumber(self, num: int) -> int:
        rst = ""
        strNum = str(num)
        if num==0:
            return 0
        if strNum[0] == "-":
            rst = "-"+"".join(sorted(strNum[1:], reverse=True))
            return int(rst)
        else:
            countZero = 0
            rst = ""
            for i in strNum:
                if i=="0":
                    countZero += 1
                else:
                    rst += i
        rst = "".join(sorted(rst))
        return int(rst[0]+"0"*countZero+rst[1:])
