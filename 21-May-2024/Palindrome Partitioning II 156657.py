# Problem: Palindrome Partitioning II - https://leetcode.com/problems/palindrome-partitioning-ii/

class Solution:
    def minCut(self, s: str) -> int:
        def isPalindrome(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        n, memo = len(s), {}
        palindrome = [[0] * n for _ in range(n)]
        for i in range(len(s)):
            for j in range(len(s)-i):
                if i == 0 or (s[j] == s[j+i] and (palindrome[j+1][j+1+i-2] or i == 1)):
                    palindrome[j][j+i] = 1
                else:
                    palindrome[j][j+i] = 0

        def dp(i):
            if i == len(s) - 1:
                return 0
            if i >= len(s):
                return -1
            if i not in memo:
                cur_min = float('inf')
                for j in range(i, len(s)):
                    if palindrome[i][j]:
                        cur_min = min(cur_min, 1 + dp(j + 1))
                memo[i] = cur_min
            return memo[i]
        
        return dp(0)