class Solution:
    def sortSentence(self, s: str) -> str:
        #def customFun(num):
        #    return num[-1]
        
        #s = sorted(s.split(), key=customFun)
        s = sorted(s.split(), key=lambda x:x[-1])
        
        return " ".join(i[:-1] for i in s)
       