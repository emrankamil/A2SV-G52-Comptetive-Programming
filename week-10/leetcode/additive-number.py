class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def validate(path):
            if len(path)<3: return False
            for i in range(2, len(path)):
                if int(path[i]) != (int(path[i-1])+int(path[i-2])):
                    return False
            return True

        def backtrack(start, path):
            if start == len(num) and validate(path):
                print(path)
                return True
            for i in range(start, len(num)):
                if (num[start] == "0" and i!= start) or (len(path)>1 and int(num[start:i+1]) != int(path[-1])+int(path[-2])):
                    continue
                path.append(num[start:i+1])
                if backtrack(i+1, path):
                    return True
                path.pop()
        return backtrack(0,[])