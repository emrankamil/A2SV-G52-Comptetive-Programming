class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        left = 0
        right = len(s)-1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        result = ""
        for i, char in enumerate(s):
            if char and result:
                result += " "+char
            elif char:
                result += char

        return result
        