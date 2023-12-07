class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = ""
        for i in range(len(spaces)):
            if i == 0:
                result += s[:spaces[i]]
            else:
                result += " "+s[spaces[i-1]:spaces[i]]

        return result+" "+s[spaces[-1]:]