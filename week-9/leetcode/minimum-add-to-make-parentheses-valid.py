class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        left = 0
        rst = 0
        for i in s:
            if i=="(":
                left += 1
            elif left:
                left -= 1
            else:
                rst += 1
        return rst+left