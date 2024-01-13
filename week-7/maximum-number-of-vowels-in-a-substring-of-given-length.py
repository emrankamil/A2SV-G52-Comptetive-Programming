class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a","e","i","o","u"}
        count_vowels = 0

        for i in range(k):
            if s[i] in vowels:
                count_vowels += 1
        
        result = count_vowels
        for i in range(k, len(s)):
            if s[i-k] in vowels:
                count_vowels -= 1
            if s[i] in vowels:
                count_vowels += 1
            result = max(result,count_vowels)

        return result