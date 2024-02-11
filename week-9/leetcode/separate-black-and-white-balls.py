class Solution:
    def minimumSteps(self, s: str) -> int:
        result = white = 0
        for i, ball in enumerate(s):
            if ball == "0":
                result += i - white
                white += 1
        return result