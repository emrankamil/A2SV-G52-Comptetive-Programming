# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        counter = [0 for _ in range(n)]
        for idx, word in enumerate(words):
            rst = 0
            for i in word:
                rst |= 1<<(ord(i)-ord('a'))
            counter[idx] = rst
        rst = 0
        for i in range(n):
            for j in range(i+1, n):
                if not counter[i]&counter[j]:
                    rst = max(rst, len(words[i])*len(words[j]))
        return rst