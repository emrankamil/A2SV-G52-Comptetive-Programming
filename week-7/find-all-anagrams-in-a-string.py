class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
            
        target = {}
        window = {}
        rst = []
        for i in range(len(p)):
            if p[i] in target:
                target[p[i]] += 1
            else:
                target[p[i]] = 1
        for i in range(len(p)-1):
            if s[i] in window:
                window[s[i]] += 1
            else:
                window[s[i]] = 1
        
        for i in range(len(p)-1, len(s)):
            if s[i] in window:
                window[s[i]] += 1
            else:
                window[s[i]] = 1

            if window == target:
                rst.append(i-len(p)+1)

            if window[s[i-len(p)+1]] == 1:
                del window[s[i-len(p)+1]]
            else:
                window[s[i-len(p)+1]] -= 1

        return rst