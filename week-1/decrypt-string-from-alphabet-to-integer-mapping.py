class Solution:
    def freqAlphabets(self, s: str) -> str:
        stack = []

        for i in s:
            if i != '#':
                stack.append(int(i))
            else:
                stack.append(stack.pop() + 10 * stack.pop())
        return "".join(chr(num + 96) for num in stack)
