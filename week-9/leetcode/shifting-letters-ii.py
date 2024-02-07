class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        total_shift  = [0]*len(s)

        accumulate = 0
        for shift in shifts:
            if shift[2] == 0:
                total_shift[shift[0]] -= 1
                if shift[1]<(len(s)-1):
                    total_shift[shift[1]+1] += 1
            else:
                total_shift[shift[0]] += 1
                if shift[1]<(len(s)-1):
                    total_shift[shift[1]+1] -= 1
        rst = []
        for i in range(len(s)):
            if i!=0:
                total_shift[i] += total_shift[i-1]
            asci = (ord(s[i])-ord('a')+total_shift[i])%26
            rst.append(chr(asci+ord('a')))

        return "".join(rst)