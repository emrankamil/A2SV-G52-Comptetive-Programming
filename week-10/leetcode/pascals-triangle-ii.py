class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        cur_pascal = [1]
        prev_pascal = self.getRow(rowIndex-1)
        for i in range(len(prev_pascal)):
            if i == (len(prev_pascal)-1):
                cur_pascal.append(1)
            else:
                cur_pascal.append(prev_pascal[i]+prev_pascal[i+1])
        return cur_pascal