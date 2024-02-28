class Solution:
    def longestNiceSubstring(self, s: str) -> str:

        for i in range(len(s)):
            if len(s)==1: return ""
            if (s[i].isupper() and s[i].lower() not in s) or (s[i].islower() and s[i].upper() not in s):

                left = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i+1:])

                if not left or len(right) > len(left):
                    return right
                elif not right or len(right) <= len(left):
                    return left
        
        return s