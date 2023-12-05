class Solution:
    def printVertically(self, s: str) -> List[str]:
        s_list = s.split()
        maxLen = len(max(s_list, key=len))

        result = []

        for i in range(maxLen):
            vertical_word = ""
            for word in s_list:
                if i < len(word):
                    vertical_word += word[i]
                else:
                    vertical_word += " "
                    
            result.append(vertical_word.rstrip())

        return result