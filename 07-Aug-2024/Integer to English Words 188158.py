# Problem: Integer to English Words - https://leetcode.com/problems/integer-to-english-words/

class Solution:
    def numberToWords(self, num: int) -> str:
        ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen",      "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        largests = ["", " Thousand", " Million", " Billion"]

        def words(n):
            if n == 0:
                return ""
            elif n < 10:
                return ones[n]
            elif 10 <= n < 20:
                return teens[n - 10]
            elif 20 <= n < 100:
                return tens[n // 10] + (" " + ones[n % 10] if (n % 10 != 0) else "")
            elif 100 <= n < 1000:
                return ones[n // 100] + " Hundred" + (" " + words(n % 100) if (n % 100 != 0) else "")
        
        rst = []
        if num == 0:
            return "Zero"
        if num < 1000:
            return words(num)
        for i in range(4):
            if num:
                n = num % 1000
                num //= 1000
                three_digits = words(n) + (largests[i] if n else "")
                if three_digits: rst.append(three_digits.strip())

        rst.reverse()
        return " ".join(rst).strip()


