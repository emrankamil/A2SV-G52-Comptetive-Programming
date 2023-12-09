
class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        full_code = "$".join(source)
        full_code += "$"
        flag = True
        new_line = ""
        result = []
        i = 0
        while i < len(full_code):
            if flag:
                if full_code[i] == "/" and full_code[i+1] =="*":
                    i += 2
                    flag = False
                elif full_code[i] == "/" and full_code[i+1] == "/":
                    while full_code[i] != "$":
                        i += 1
                    i -= 1
                elif full_code[i] == "$":
                    if new_line:
                        result.append(new_line)
                    else:
                        i += 1
                        continue
                    new_line = ""
                else:
                    new_line += full_code[i]
            elif full_code[i] == "/" and full_code[i-1] == "*":
                flag = True    
        
            i += 1
        return result

        """
        Made by: Yohannes and Emran

        """
