class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)

        if n > m:
            return False
            
        target = {}
        window = {}

        for i in range(n):
            if s1[i] in target:
                target[s1[i]] += 1
            else:
                target[s1[i]] = 1
        
        for i in range(n-1):
            if s2[i] in window:
                window[s2[i]] += 1
            else:
                window[s2[i]] = 1
        
        for i in range(n-1, m):
            if s2[i] in window:
                window[s2[i]] += 1
            else:
                window[s2[i]] = 1
            
            if window == target:
                return True
            
            if window[s2[i-n+1]] == 1:
                del window[s2[i-n+1]]
            else:
                window[s2[i-n+1]] -= 1
        
        return False