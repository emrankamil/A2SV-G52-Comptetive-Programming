# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = set()
        n = len(s)
        for i in range(1<<n):
            buf = ''
            for j in range(n):
                if i & (1<<j) > 0:
                    buf += s[j].lower()
                else:
                    buf += s[j].upper()
            result.add(buf)
        return result