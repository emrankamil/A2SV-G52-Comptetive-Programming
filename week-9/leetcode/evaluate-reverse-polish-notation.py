class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ["+","-","*","/"]:
                a = stack.pop()
                b = stack.pop()
                if token == "+":
                    stack.append(int(b) + int(a))
                elif token == "-":
                    stack.append(int(b) - int(a))
                elif token == "*":
                    stack.append(int(b) * int(a))
                else:
                    stack.append(int(b) / int(a))
            else:
                stack.append(token)
        
        return int(stack[0])