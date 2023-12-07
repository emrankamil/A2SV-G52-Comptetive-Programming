class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = ("qwertyuiop")
        second_row = ("asdfghjkl")
        third_row = ("zxcvbnm")
        
        result = []

        for word in words:
            rst = ""
            if word[0].lower() in first_row:
                row = first_row
            elif word[0].lower() in second_row:
                row = second_row
            else:
                row = third_row
            for i in range(1, len(word)):
                if word[i].lower() not in row:
                    break
            else:
                rst = word

            if rst:
                result.append(rst)

        return result