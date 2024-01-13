class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        window = {}
        rst = 0
        for r in range(len(s)):
            if s[r] in window and window[s[r]] >= l:
                l = window[s[r]]+1
            window[s[r]] = r
            rst = max(rst, r-l+1)
           
        return rst
