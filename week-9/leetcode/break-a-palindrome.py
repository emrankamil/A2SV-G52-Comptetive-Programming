class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n==1:
            return ""
        for i in range(n):
            if (n%2 and i==n//2):
                continue
            elif palindrome[i]=="a" and i==n-1:
                return palindrome[:-1]+"b"             
            elif palindrome[i]!="a":
                return palindrome[:i]+"a"+palindrome[i+1:]
        return ""