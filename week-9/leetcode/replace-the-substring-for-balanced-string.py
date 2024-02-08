class Solution:
        
    def balancedString(self, s: str) -> int:

        def contain(window, check):
            for i in window:
                if window[i] < check[i]:
                    return False
            return True

        count = Counter(s)
        req = {"Q":0, "W":0, "E":0,"R":0}

        for i in count:
            if count[i] > len(s)//4:
                req[i] = count[i]-len(s)//4
        window = {"Q":0, "W":0, "E":0,"R":0}
        left = 0
        rst = len(s)

        for i in range(len(s)):
            window[s[i]] += 1
            while contain(window, req):
                rst = min(rst, i-left+1)   
                if left>i: 
                    break
                window[s[left]] -= 1
                left += 1
        return rst


        


        
        
    