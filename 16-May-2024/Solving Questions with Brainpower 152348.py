# Problem: Solving Questions with Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * n
        for i in range(n-1, -1, -1):
            score, power = questions[i]
            op1 = score + dp[i + power + 1] if power + i + 1 < n else score
            op2 = dp[i + 1] if i + 1 < n else 0
            dp[i] = max(op1, op2)
        return dp[0]