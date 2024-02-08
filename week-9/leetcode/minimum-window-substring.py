class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""

        t_check = Counter(t)
        window = defaultdict(int)

        left = 0
        rst = [0,len(s)+1]
        for i in range(len(s)):
            window[s[i]] += 1
            while self.contain(window, t_check):
                if i-left+1 < rst[1]-rst[0]:
                    rst = [left, i+1]
                if left>i:
                    break
                window[s[left]] -= 1
                left += 1
        if rst[1] < len(s)+1:
            return s[rst[0]:rst[1]]
        return ""

    def contain(self,window, req):
        for i in req:
            if window[i]<req[i]:
                return False
        return True
        
# t_check = [0]*52
# for i in t:
#     if i.isupper():
#         t_check[ord(i)-ord("A")+26] += 1
#     else:
#         t_check[ord(i)-ord("a")] += 1