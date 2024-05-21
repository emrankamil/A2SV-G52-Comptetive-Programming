# Problem: Palindrome Partitioning - https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
            
        memo = {}
        def dp(i):
            if i >= len(s) - 1:
                return [s[i:]]
                
            if i in memo:  return memo[i]

            part = []
            for j in range(i, len(s)):
                if isPalindrome(i, j):
                    _next = dp(j + 1)
                    for p in _next:
                        cur = [s[i:j + 1]]
                        cur.extend(p)
                        part.append(cur)
            memo[i] = part
            return memo[i]

        return dp(0)