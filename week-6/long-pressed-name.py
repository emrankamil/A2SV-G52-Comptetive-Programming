class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j = 0, 0
        if len(typed) < len(name):
            return False
        while i < len(name) and j < len(typed):
            if name[i] == typed[j]:
                i += 1
                j += 1
            elif j == 0 or typed[j] != typed[j - 1]:
                return False
            else:
                j += 1
        return i == len(name) and typed[j:] == typed[j - 1] * (len(typed) - j)