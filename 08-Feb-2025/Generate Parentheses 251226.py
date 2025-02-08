# Problem: Generate Parentheses - https://leetcode.com/problems/generate-parentheses/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(left, right, current):
            if right == n:
                result.append("".join(current))
                return
            if left > right:
                backtrack(left, right+1, current + [')'])
            if left < n:
                backtrack(left+1, right, current + ['('])

        backtrack(0, 0, [])
        return result