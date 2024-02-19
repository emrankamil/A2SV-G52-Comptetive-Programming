class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        depth = 0
        res = 0
        prev = '('
        
        for ch in s:
            if ch == '(':
                depth += 1
            else:
                depth -= 1
                if prev == '(':
                    res += 2 ** depth
            
            prev = ch
        
        return res
