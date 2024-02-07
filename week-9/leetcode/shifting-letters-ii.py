class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        total_shift = [0]*len(s)
        for shift in shifts:
            if shift[2] == 0:
                shift[2] = -1
            
            total_shift[shift[0]] += shift[2]
            if shift[1] != len(s)-1:
                total_shift[shift[1]+1] -= shift[2]
        
        accumulate = 0
        for i in range(len(total_shift)):
            accumulate += total_shift[i]
            total_shift[i] = accumulate
        
        result = ""
        for i in range(len(s)):
            asci = (ord(s[i])-ord('a')+total_shift[i])%26
            result += chr(asci+ord('a'))

        return result
        