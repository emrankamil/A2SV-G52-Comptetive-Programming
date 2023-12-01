class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minStr = ""
        minLen = float('inf')
        for i in strs:
            if len(i)<minLen:
                minStr = i
                minLen = len(i)
        rst = ""
        for i in range(minLen):
            for string in strs:
                if string[i] != minStr[i]:
                    return rst
            rst += minStr[i]

        return rst