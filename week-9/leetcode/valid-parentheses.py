class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {'(':')', '[':']', '{':'}'}
        
        for i in s:
            if i in parentheses:
                stack.append(i)
            else:
                if stack and i == parentheses[stack[-1]]:
                    stack.pop()
                else:
                    return False
        if len(stack):
            return False
        return True
            
        