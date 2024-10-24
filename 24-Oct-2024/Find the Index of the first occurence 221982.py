# Problem: Find the Index of the first occurence - https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(needle), len(haystack)
        if n < m:
            return -1

        needle_hash = 0
        cur_hash = 0

        for i in range(m):
            needle_hash += (ord(needle[i]) - ord('a') + 1) * (26 ** (m - i - 1))
            cur_hash += (ord(haystack[i]) - ord('a') + 1) * (26 **  (m - i - 1))
            
        for i in range(m, n):
            if needle_hash == cur_hash:
                return i - m
            
            cur_hash -= (ord(haystack[i - m]) - ord('a') + 1) * (26 ** (m - 1))
            cur_hash *= 26
            cur_hash += ord(haystack[i]) - ord('a')  + 1

        
        return n - m if needle_hash == cur_hash else -1